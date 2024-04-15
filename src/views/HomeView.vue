<script setup>

</script>

<template>
  <div>
    <div class="card">
      <div class="card-body">
        <div id="carouselExampleIndicators" class="carousel slide ">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
                <div class="carousel-item-body">
                  <img src="https://culturaenjuego.ar/fotos/0_whatsappimage2023-09-30at8.47.02pm1.jpg" alt="...">
                </div>
            </div>
            <div class="carousel-item">
              <div class="carousel-item-body">
                <img src="https://culturaenjuego.ar/fotos/dsc06390.jpg" alt="...">
              </div>
            </div>
            <div class="carousel-item">
              <div class="carousel-item-body">
                <img src="https://culturaenjuego.ar/fotos/p1010048.jpg" alt="...">
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
      
    <!-- <div class="container">
      <div class="card" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <h6 class="card-subtitle mb-2 text-body-secondary">Card subtitle</h6>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <a href="#" class="card-link">Card link</a>
          <a href="#" class="card-link">Another link</a>
        </div>
      </div>
    </div> -->
  </div>
</template>


<style scoped>
@media screen and (max-width: 768px) {
  .carousel-item-body {
    height: 300px;
  }
}

@media screen and (min-width: 768px) {
  .carousel-item-body {
    height: 600px;
  }
}

img {
  height: 100%;
  max-width: 100%;
  object-fit: contain;
}

.card {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 50px;
  margin-right: 50px;
}
</style>