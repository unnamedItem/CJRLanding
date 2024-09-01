<script setup>
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
  } else {
    return 'light';
  }
}

const props = defineProps({
    item: Object
})
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
              <small>{{ item.yearpublished }}</small>
              <abbr :title="Number(item.bggRating || item.averageRating).toFixed(2)">
                <div>
                  <i v-for="i in 5" :key="i" v-bind:class="['text-warning', setStars(i, item.bggRating || item.averageRating)]"></i>
                </div>
              </abbr>
            </div>
            <hr class="my-2">
            <table class="table table-borderless">
              <tr>
                <td>Jugadores</td>
                <td class="d-flex justify-content-end">{{ item.minPlayers }} - {{ item.maxPlayers }}</td>
              </tr>
              <tr>
                <td>Tiempo de juego</td>
                <td class="d-flex justify-content-end">{{ setPlayTime(item.playingTime, item.playingTime) }} Min.</td>
              </tr>
              <!-- <tr>
                <td>Edad: </td>
                <td class="d-flex justify-content-end">+{{ item.age }}</td>
              </tr> -->
              <!-- <tr>
                <td>Complejidad</td>
                <td class="d-flex justify-content-end"><span :class="setAvgWeight(item.averageweight)">{{ item.averageweight.toFixed(1) }} / 5</span></td>
              </tr> -->
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

span {
  background-color: transparent;
  margin: 0;
  padding: 0;
}
</style>