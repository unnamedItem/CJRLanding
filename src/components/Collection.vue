<script setup>
import { ref, watchEffect, onUpdated, computed } from "vue"
import { useRoute } from 'vue-router';
import CollectionItem from '@/components/CollectionItem.vue'

const API_URL = `/games.json`;

// =============================================================================
// Variables
const result = ref(null);
const collectionCopy = ref(null);
const search = ref(useRoute().query.search || '');
const playingTime = ref(null);
const numberOfPlayers = ref(null);
const weight = ref(null);
const age = ref(null);
const categories = ref(null);
const filterCollapsed = ref(false);
const locales = ref({});

// =============================================================================
// Watchers
watchEffect(async () => {
  result.value = await ((await fetch(API_URL)).text()); 
})

watchEffect(() => {
  if (result.value) {
    collectionCopy.value = JSON.parse(result.value);
  }
})

watchEffect(async () => {
  locales.value = await fetch('/locales.json').then(res => res.json());
})

// =============================================================================
// Functions
const filterByName = (items, name) => {
  if (!name) return items
  return items.filter(item => item.name.toLowerCase().includes(name.toLowerCase()))
}

const filterByPlayers = (items, players) => {
  if (!players) return items
  return items.filter(item => parseInt(item.minplayers) <= players && parseInt(item.maxplayers) >= players)
}

const filterByPlayingTime = (items, playtime) => {
  if (!playtime) return items
  return items.filter(item => parseInt(item.minplaytime) <= playtime && parseInt(item.maxplaytime) >= playtime)
}

const filterByWeight = (items, weight) => {
  if (!weight) return items
  return items.filter(item => item.averageweight >= weight[0] && item.averageweight <= weight[1])
}

const filterByAge = (items, age) => {
  if (!age) return items
  return items.filter(item => parseInt(item.age) <= parseInt(age))
}

const filterByCategories = (items, category) => {
  if (!category) return items
  return items.filter(item => item.boardgamesubdomain.split(', ').includes(category))
}

const clearFilters = () => {
  search.value = '';
  numberOfPlayers.value = null;
  playingTime.value = null;
  weight.value = null;
  age.value = null;
  categories.value = null;
}

const t = (txt) => {
  return locales.value[txt]
} 

const onSubdomain = (subdomain) => {
  categories.value = subdomain != 'Juego' ? subdomain : null;
}

// =============================================================================
// Computed
const collection = computed(() => {
  if (collectionCopy.value) {
    let filtered = collectionCopy.value;
    filtered = filterByName(filtered, search.value);
    filtered = filterByPlayers(filtered, numberOfPlayers.value);
    filtered = filterByPlayingTime(filtered, playingTime.value);
    filtered = filterByWeight(filtered, weight.value);
    filtered = filterByAge(filtered, age.value);
    filtered = filterByCategories(filtered, categories.value);
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

const avgWeightOptions = computed(() => {
  return [
    { value: [0, 1.5], text: 'Facil' },
    { value: [1.5, 2.5], text: 'Intermedio' },
    { value: [2.5, 3.5], text: 'Avanzado' },
    { value: [3.5, 5], text: 'Muy Dificil' },
  ];
})

const ageOptions = computed(() => {
  if (collectionCopy.value) {
    let age = collectionCopy.value.map(item => item.age);
    let filtered = age.filter(item => item !== 0);
    return [...new Set([...filtered])].sort((a, b) => a - b);
  }
  return [];
})

const categoryOptions = computed(() => {
  if (collectionCopy.value) {
    let categories = collectionCopy.value.map(item => item.boardgamesubdomain.split(', ')).flat();
    let filtered = categories.filter(item => item !== "");
    return [...new Set([...filtered])].sort((a, b) => a - b);
  }
  return [];
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
    <div class="col-xxl-3 col-12">
      <div class="card mb-3">
        <!-- SEARCH FILTER -->
        <div class="card-body">
          <h4>Filtros</h4>
          <hr>
          <form @action.prevent="" class="collapse" id="filters">            
            <!-- NAME -->
            <div class="mb-3">
              <label class="form-label">Titulo</label>
              <input type="text" class="form-control mb-3" v-model="search" placeholder="Buscar...">
            </div>
            <!-- PLAYERS -->
            <div class="mb-3 row">
              <label class="form-label">Cantidad de Jugadores</label>
              <div class="col">
                <select class="form-select" v-model="numberOfPlayers">
                  <option :value="null">Cualquier Número</option>
                  <option v-for="player in playersOptions" :key="player" :value="player">{{ player }}</option>
                </select>
              </div>
            </div>
            <!-- PLAYTIME -->
            <div class="mb-3 row">
              <label class="form-label">Tiempo de Juego</label>
              <div class="col">
                <select class="form-select" v-model="playingTime">
                  <option :value="null">Cualquier Duración</option>
                  <option v-for="time in playTimeOptions" :key="time" :value="time">{{ time }}</option>
                </select>
              </div>
            </div>
            <!-- WEIGHT -->
            <div class="mb-3 row">
              <label class="form-label">Difultad</label>
              <div class="col">
                <select class="form-select" v-model="weight">
                  <option :value="null">Todas las Difultades</option>
                  <option v-for="w in avgWeightOptions" :key="w" :value="w.value">{{ w.text }}</option>
                </select>
              </div>
            </div>
            <!-- AGE -->
            <div class="mb-3 row">
              <label class="form-label">Edad</label>
              <div class="col">
                <select class="form-select" v-model="age">
                  <option :value="null">Todas las Edades</option>
                  <option v-for="a in ageOptions" :key="a" :value="a">{{ a }}</option>
                </select>
              </div>
            </div>
            <!-- CATEGORIES -->
            <div class="mb-3 row">
              <label class="form-label">Categoria</label>
              <div class="col">
                <select class="form-select" v-model="categories">
                  <option :value="null">Todas las Categorias</option>
                  <option v-for="tag in categoryOptions" :key="tag" :value="tag">{{ t(tag) }}</option>
                </select>
              </div>
            </div>
            <div class="col mt-4">
              <button class="btn btn-primary mb-3 w-100" @click.prevent="clearFilters()">
                <span>Limpiar Filtros</span>
              </button>
            </div>
          </form>
          <button class="btn btn-primary mb-3 w-100" data-bs-toggle="collapse" data-bs-target="#filters" @click="filterCollapsed = !filterCollapsed">
            <i :class="{'bi bi-caret-down-fill': !filterCollapsed, 'bi bi-caret-up': filterCollapsed}"></i>
          </button>
        </div>
      </div>
    </div>
    
    <!-- COLLECTION -->
    <div class="col-xxl-9 col-12">
      <div class="row">
        <div v-for="(item, index) in collection" :key="index" class="col-lg-6 col-xl-4">
          <CollectionItem :item="item" @subdomain="onSubdomain($event)"></CollectionItem>
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
