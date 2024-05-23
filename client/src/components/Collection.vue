<script setup>
import { ref, watchEffect, onUpdated, computed } from "vue"
import { useRoute } from 'vue-router';
import CollectionItem from '@/components/CollectionItem.vue'

const API_URL = `https://bgg-json.azurewebsites.net/collection/clubdejuegosrosario`;

const result = ref(null);
const collectionCopy = ref(null);
const search = ref(useRoute().query.search || '');
// const playingTimeFrom = ref(null);
// const playingTimeTo = ref(null);
// const numberOfPlayersFrom = ref(null);
// const numberOfPlayersTo = ref(null);

const collection = computed(() => {
  if (collectionCopy.value) {
    let filtered = collectionCopy.value;
    filtered = filterByName(filtered, search.value);
    // filtered = filterByPlayingTime(filtered, playingTime.value);
    // filtered = filterByNumberOfPlayers(filtered, numberOfPlayers.value);
    return filtered;
  } else {
    return [];
  }
})

const filterByName = (items, name) => {
  if (!name) return items
  return items.filter(item => item.name.toLowerCase().includes(name.toLowerCase()))
}

// const filterByPlayingTime = (items, time) => {
//   if (!time) return items
//   return items.filter(item => item.minPlaytime <= time && item.maxPlaytime >= time)
// }

// const filterByNumberOfPlayers = (items, players) => {
//   if (!players) return items
//   return items.filter(item => item.minPlayers <= players && item.maxPlayers >= players)
// }

watchEffect(async () => {
  result.value = await (await fetch(API_URL)).text(); 
})

watchEffect(() => {
  if (result.value) {
    collectionCopy.value = JSON.parse(result.value);
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
    <!-- <div class="col-12 card my-3 p-3">
      <form class="row">
        <div class="form-group col-lg-4 my-auto">
          <input id="search" v-model="search" placeholder="Buscar un juego" type="text" class="form-control">
        </div>
        <div class="form-group col-lg-3 my-auto">
          <label for="playingTime">Tiempo de juego</label>
          <input id="playingTime" v-model="playingTime" type="number" class="form-control">

        </div>
        <div class="form-group col-lg-3 my-auto">
          <label for="numberOfPlayers">Número de jugadores</label>
          
        </div>
      </form>
    </div> -->

    <div v-for="(item, index) in collection" :key="index" class="col-md-6 col-lg-4">
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
