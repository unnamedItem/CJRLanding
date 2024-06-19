<script setup>
import { ref, watchEffect, onUpdated, computed } from "vue"
import { useRoute } from 'vue-router';
import CollectionItem from '@/components/CollectionItem.vue'

const API_URL = `http://localhost:8000/api/games`;

// =============================================================================
// Variables
const result = ref(null);
const collectionCopy = ref(null);
const search = ref(useRoute().query.search || '');
const playingTimeFrom = ref(null);
const playingTimeTo = ref(null);
const numberOfPlayersFrom = ref(null);
const numberOfPlayersTo = ref(null);



// =============================================================================
// Computed
const collection = computed(() => {
  if (collectionCopy.value) {
    let filtered = collectionCopy.value;
    filtered = filterByName(filtered, search.value);
    filtered = filterByPlayers(filtered, numberOfPlayersFrom.value, numberOfPlayersTo.value);
    filtered = filterByPlayingTime(filtered, playingTimeFrom.value, playingTimeTo.value);
    return filtered;
  } else {
    return [];
  }
})

const playersOptions = computed(() => {
  if (collectionCopy.value) {
    let maxplayers = collectionCopy.value.map(item => item.maxplayers)
    let minplayers = collectionCopy.value.map(item => item.minplayers)
    return [...new Set([...maxplayers, ...minplayers])].sort((a, b) => a - b);
  }
  return [];
})

const playTimeOptions = computed(() => {
  if (collectionCopy.value) {
    let maxplaytime = collectionCopy.value.map(item => item.maxplaytime)
    let minplaytime = collectionCopy.value.map(item => item.minplaytime)
    return [...new Set([...maxplaytime, ...minplaytime])].sort((a, b) => a - b);
  }
  return [];
})

// =============================================================================
// Functions
const filterByName = (items, name) => {
  if (!name) return items
  return items.filter(item => item.name.toLowerCase().includes(name.toLowerCase()))
}

const filterByPlayers = (items, minplayers, maxplayers) => {
  if (!minplayers || !maxplayers) return items
  if (!maxplayers) return items.filter(item => item.minplayers >= minplayers)
  if (!minplayers) return items.filter(item => item.maxplayers <= maxplayers)
  return items.filter(item => item.minplayers >= minplayers && item.maxplayers <= maxplayers)
}

const filterByPlayingTime = (items, minplaytime, maxplaytime) => {
  if (!minplaytime || !maxplaytime) return items
  if (!maxplaytime) return items.filter(item => item.minplaytime >= minplaytime)
  if (!minplaytime) return items.filter(item => item.maxplaytime <= maxplaytime)
  return items.filter(item => item.minplaytime >= minplaytime && item.maxplaytime <= maxplaytime)
}

// =============================================================================
// Watchers
watchEffect(async () => {
  result.value = await (await fetch(API_URL)).text(); 
})

watchEffect(() => {
  if (result.value) {
    collectionCopy.value = JSON.parse(result.value);
    
  }
})

// =============================================================================
// Intersection Observer
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
    <div class="col-xl-3 col-12">
      <div class="card d-none d-xl-block">
        <!-- SEARCH FILTER -->
        <div class="card-body">
          <form @action.prevent="">
            <!-- NAME -->
            <div class="mb-3">
              <label class="form-label">Nombre</label>
              <input type="text" class="form-control mb-3" v-model="search">
            </div>
            <!-- PLAYERS -->
            <div class="mb-3 row">
              <label class="form-label">Cantidad de Jugadores</label>
              <div class="col-5">
                <select class="form-select" v-model="numberOfPlayersFrom">
                  <option :value="null">Min. Players</option>
                  <option v-for="player in playersOptions" :key="player" :value="player">{{ player }}</option>
                </select>
              </div>
              <div class="col-2 text-center">
                -
              </div>
              <div class="col-5">
                <select class="form-select" v-model="numberOfPlayersTo">
                  <option :value="null">Max. Players</option>
                  <option v-for="player in playersOptions" :key="player" :value="player">{{ player }}</option>
                </select>
              </div>
            </div>
            <!-- PLAYTIME -->
            <div class="mb-3 row">
              <label class="form-label">Tiempo de Juego</label>
              <div class="col-5">
                <select class="form-select" v-model="playingTimeFrom">
                  <option :value="null">Min. Time</option>
                  <option v-for="time in playTimeOptions" :key="time" :value="time">{{ time }}</option>
                </select>
              </div>
              <div class="col-2 text-center">
                -
              </div>
              <div class="col-5">
                <select class="form-select" v-model="playingTimeTo">
                  <option :value="null">Max. Time</option>
                  <option v-for="time in playTimeOptions" :key="time" :value="time">{{ time }}</option>
                </select>
              </div>
            </div>
            <!-- WEIGHT -->

            <!-- AGE -->

            <!-- TAGS -->
          </form>
        </div>
      </div>
    </div>
    <!-- COLLECTION -->
    <div class="col-xl-9 col-12">
      <div class="row">
        <div v-for="(item, index) in collection" :key="index" class="col-lg-6 col-xl-4">
          <CollectionItem :item="item"></CollectionItem>
        </div>
      </div>
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

.card {
  position: sticky;
  top: 20px;
  overflow-y: auto;
  max-height: 75vh;
  scrollbar-color: rgba(0, 0, 0, 0.5) transparent;
}
</style>
