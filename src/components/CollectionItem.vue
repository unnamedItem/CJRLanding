<script setup>
const props = defineProps({
    item: Object
})
</script>

<template>
    <div class="card-item">
        <div class="image-container">
            <img :src="item.image.text" alt="Card Image" class="card-image" />
        </div>
        <div class="card-details">
            <h3 class="card-title">{{ item.name.text }}</h3>
            <p class="card-description">{{ item.name.text }}</p>
        </div>
    </div>
</template>

<style scope>
.card-item {
  display: flex;
  border: 1px solid #ddd;
  margin: 10px;
  padding: 10px;
  border-radius: 5px;
}

.card-image {
  width: 200px; /* Set your desired width */
  height: 200px;
  margin-right: 10px;
  object-fit: contain;
}

.card-details {
  flex-grow: 1;
  margin-left: 10px;
}

.card-title {
  font-size: 1.2rem;
  margin-bottom: 5px;
}

.card-description {
  font-size: 1rem;
}

.image-container {
    background-color: #ddd;
    border: 5px solid #ddd;
    border-radius: 5px;
}
</style>