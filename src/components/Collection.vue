<script setup>
import { ref, watchEffect, onUpdated } from "vue"
import CollectionItem from '@/components/CollectionItem.vue'

const API_URL = `https://bgg-json.azurewebsites.net/collection/clubdejuegosrosario`;

const collection = ref(null);

watchEffect(async () => {
  collection.value = await (await fetch(API_URL)).text(); 
})

watchEffect(async () => {
  if (collection.value) {
    collection.value = JSON.parse(collection.value);
  }
})

onUpdated(() => {
  const hiddenSections = document.querySelectorAll('.hidden');

  const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
          entry.target.classList.toggle('show', entry.isIntersecting);
      });
  } );

  hiddenSections.forEach((seccion)=>observer.observe(seccion));
})
</script>

<template>
  <div v-if="collection" class="row">
    <div v-for="(item, index) in collection" :key="index" class="col-md-4">
      <CollectionItem :item="item"></CollectionItem>
    </div>
  </div>

  <div class="loading-blur" v-if="!collection">
    <div class="spinner-border text-secondary" role="status">
      <span class="sr-only"></span>
    </div>
  </div>
</template>

<style scoped>
.loading-blur {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backdrop-filter: blur(5px);
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;
}
</style>
