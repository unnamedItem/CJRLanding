<script setup>
import { ref, watchEffect } from "vue"
import { xmlToJson } from '@/utils/xml2json'
import CollectionItem from '@/components/CollectionItem.vue'

const API_URL = `https://boardgamegeek.com/xmlapi/collection/clubdejuegosrosario`;
const Parser = new DOMParser();

const collection = ref(null);

watchEffect(async () => {
  collection.value = await (await fetch(API_URL)).text(); 
})

watchEffect(async () => {
  if (collection.value) {
    let xmlDoc = Parser.parseFromString(collection.value, "text/xml");
    collection.value = xmlToJson(xmlDoc);
    console.log(collection)
  }
})
</script>

<template>
  <div v-if="collection">
    <CollectionItem v-for="(item, index) in collection.items.item" :key="index" :item="item"></CollectionItem>
  </div>
</template>

<style scoped>

</style>
