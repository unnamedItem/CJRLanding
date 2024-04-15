<script setup>
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <Navbar />
  <div class="main">
    <RouterView />
  </div>
  <Footer />
</template>

<style scoped>
nav {
    background-color: rgb(0, 0, 0, 0.5);
    min-height: 8vh;
    font-size: large;
}

.footer {
    width: 100%;
    height: 8vh;
    background-color: rgb(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--bs-background);
    text-align: center;
    bottom: 0;
}

.main {
    min-height: 84vh;
    overflow: auto;
    padding-top: 2vh;
    padding-bottom: 2vh;
    scrollbar-color: rgba(0, 0, 0, 0.5) transparent;
}
</style>
