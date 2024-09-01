<script setup>
import { useRoute } from 'vue-router';
const searchGame = (event) => {
  window.location.href = `/collection?search=${event.target[0].value}`
}
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">
        <img src="../assets/logo.png" alt="Logotipo" width="50" height="50" class="d-inline-block align-middle">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" aria-current="page" href="/">Inicio</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/#events">Eventos</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/#about">Sobre Nosotros</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/#contact">Redes</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/collection">Ludoteca</a>
          </li>
        </ul>
        <form class="d-flex" role="search" @submit.prevent="searchGame($event)">
          <input class="form-control me-2" type="search" placeholder="Buscar un juego" aria-label="Search">
          <button id="search" class="btn btn-primary" type="submit">Buscar</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  z-index: 200;
}

.nav-item {
  margin-right: 1.5rem;
}
</style>