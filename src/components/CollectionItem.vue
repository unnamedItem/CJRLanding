<script setup>
const props = defineProps({
    item: Object
})
</script>

<template>
  <div class="card mb-3" style="max-width: 540px;">
    <div class="row g-0">
      <div class="col-md-4">
        <img :src="item.image.text" alt="Card Image" class="card-image" />
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <h5 class="card-title">{{ item.name.text }}</h5>
          <p class="card-text">{{ item.name.text }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scope>
.card-image {
  height: 200px;
  width: 100%;
  object-fit: contain;
  padding: 10px;
}
</style>