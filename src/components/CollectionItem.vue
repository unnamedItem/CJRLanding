<script setup>
import { ref, watchEffect, computed } from "vue"

const WEIGHT_OFFSET = .25

const locales = ref({});

function setStars(i, rating) {
  if (i * 2 <= rating) {
    return 'bi bi-star-fill';
  } else if (i * 2 - 1 <= rating) {
    return 'bi bi-star-half';
  } else {
    return 'bi bi-star';
  }
}

function setPlayTime(min, max) {
  if (min == max) {
    return min;
  } else {
    return min + ' - ' + max;
  }
}

function setAvgWeight(avg) {
  if (avg == 5) {
    return 'deadly';
  } else if (avg > 4) {
    return 'heavy';
  } else if (avg > 3) {
    return 'medium-heavy';
  } else if (avg > 2) {
    return 'medium';
  } else if (avg > 1) {
    return 'medium-light';
  } else if (avg > 0) {
    return 'light';
  } else {
    return 'no-weight';
  }
}

function setAvgWeightIcons(i, avg) {
  if (i - WEIGHT_OFFSET <= avg) {
    return 'bi bi-hexagon-fill';
  } else if (i - 1 < avg) {
    return 'bi bi-hexagon-half';
  } else {
    return 'bi bi-hexagon';
  }
}

function setAvgWeightAbbr(avg) {
  return avg == 0 ? 'Sin datos' : avg;
}

const props = defineProps({
    item: Object
})

const subDomains = computed(() => {
  if (props.item) {
    return props.item.boardgamesubdomain.split(', ').map(sub => sub !== '' ? sub : 'Juego');
  }
})

const avgWeight = computed(() => {
  if (props.item) {
    return props.item.averageweight.toFixed(2);
  }
})

watchEffect(async () => {
  locales.value = await fetch('/locales.json').then(res => res.json());
})

const t = (txt) => {
  return locales.value[txt]
} 
</script>

<template>
  <a :href="`https://boardgamegeek.com/boardgame/${item.objectid}`" target="_blank">
    <div class="card my-2 hidden">
      <div class="row g-0">
        <div class="col-md-4">
          <div class="card-image-container">
            <img :src="item.image" alt="Card Image" class="card-image" />
          </div>
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <abbr :title="item.name" style="text-decoration: none;"><h6 class="card-title">{{ item.name }}</h6></abbr>
            <div class="d-flex justify-content-between">
              <div>
                <small v-for="sub in subDomains"><span class="mx-1" @click.prevent="$emit('subdomain', sub)">
                  <abbr :title="t(sub)">
                    <img v-if="sub == 'Party Games'" src="../assets/icons/party.svg" width="25px" height="25px">
                    <img v-else-if="sub == 'Children\'s Games'" src="../assets/icons/childs.svg" width="25px" height="25px">
                    <img v-else-if="sub == 'Family Games'" src="../assets/icons/family.svg" width="25px" height="25px">
                    <img v-else-if="sub == 'Strategy Games'" src="../assets/icons/strategy.svg" width="25px" height="25px">
                    <img v-else-if="sub == 'Abstract Games'" src="../assets/icons/abstract.svg" width="25px" height="25px">
                    <img v-else-if="sub == 'Thematic Games'" src="../assets/icons/history.svg" width="25px" height="25px">
                    <img v-else src="../assets/icons/dice.svg" width="25px" height="25px">
                  </abbr>
                </span></small>
              </div>
              <small>{{ item.yearPublished }}</small>
              <abbr :title="Number(item.average).toFixed(2)">
                <div>
                  <i v-for="i in 5" :key="i" v-bind:class="['text-warning', setStars(i, item.average)]"></i>
                </div>
              </abbr>
            </div>
            <hr class="my-2">
            <table class="table table-borderless">
              <tr>
                <td><i class="bi bi-people-fill p-0" style="background-color: transparent; color: white;"></i> Jugadores</td>
                <td class="d-flex justify-content-end">{{ item.minplayers }} - {{ item.maxplayers }}</td>
              </tr>
              <tr>
                <td><i class="bi bi-hourglass-split p-0" style="background-color: transparent; color: white;"></i> Duración</td>
                <td class="d-flex justify-content-end">{{ setPlayTime(item.minplaytime, item.maxplaytime) }} Min.</td>
              </tr>
              <tr>
                <td><i class="bi bi-person-arms-up p-0" style="background-color: transparent; color: white;"></i> Edad</td>
                <td class="d-flex justify-content-end">+{{ item.age }}</td>
              </tr>
              <tr>
                <td><i class="bi bi-gear-fill p-0" style="background-color: transparent; color: white;"></i> Complejidad</td>
                <td class="d-flex justify-content-end">
                  <abbr :title="setAvgWeightAbbr(avgWeight)" style="background-color: transparent;" class="p-0">
                    <i v-for="i in 5" :key="i":class="[setAvgWeightIcons(i, avgWeight), setAvgWeight(avgWeight)]"></i>
                  </abbr>
                </td>
              </tr>
            </table>
          </div>
        </div>
      </div>
    </div>
  </a>
</template>

<style scoped>
.card-image-container {
  height: 100%;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 5px;
}

.card-image {
  height: 20vh;
  width: 100%;
  object-fit: contain;
}

.hidden {
  opacity:0;
  transform:scale(0.8);
  transition: all ease-out 1.2s;
}

.show {
  opacity:1;
  transform:scale(1);  
}

.card-title {
  background-color: rgba(255, 255, 255, 0.1);
  padding: 5px;
  border-radius: 5px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 100%;
}

small {
  font-style: italic;
}

.card {
  cursor: pointer;
  font-size: 14px;
}

.card:hover {
  background-color: rgba(0, 0, 0, 0.6);
}

a {
  text-decoration: none;
}

.pill {
  background-color: rgba(131, 16, 16, 0.25);
}

.deadly {
  color: rgb(87, 2, 2);
}

.heavy {
  color: rgb(255, 0, 0);
}

.medium-heavy {
  color: rgb(255, 128, 0);
}

.medium {
  color: rgb(255, 255, 0);
}

.medium-light {
  color: rgb(0, 255, 0);
}

.light {
  color: rgb(0, 255, 255);
}

.no-weight {
  color: gray;
}

span {
  background-color: transparent;
  margin: 0;
  padding: 0;
}

.badge {
    background-color: var(--bs-background) !important;
}
</style>