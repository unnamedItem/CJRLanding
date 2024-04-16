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

const props = defineProps({
    item: Object
})
</script>

<template>
  <div class="card my-2 hidden">
    <div class="row g-0">
      <div class="col-md-4">
        <img :src="item.image" alt="Card Image" class="card-image" />
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <h5 class="card-title">{{ item.name }}</h5>
          <div class="d-flex justify-content-between">
            <small>{{ item.yearPublished }}</small>
            <abbr :title="Number(item.averageRating).toFixed(2)">
              <div>
                <i v-for="i in 5" :key="i" v-bind:class="['text-warning', setStars(i, item.averageRating)]"></i>
              </div>
            </abbr>
          </div>
          <hr>
          <table class="table table-borderless">
            <tr>
              <td>Jugadores</td>
              <td class="d-flex justify-content-end">{{ item.minPlayers }} - {{ item.maxPlayers }}</td>
            </tr>
            <tr>
              <td>Tiempo de juego</td>
              <td class="d-flex justify-content-end">{{ item.playingTime }} Min.</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-image {
  height: 20vh;
  width: 100%;
  object-fit: contain;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 5px;
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
}

small {
  font-style: italic;
}
</style>