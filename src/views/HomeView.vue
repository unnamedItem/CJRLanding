<template>
  <div class="home">
    <!-- Encabezado -->
    <header id="inicio" class="jumbotron jumbotron-fluid text-center bg">
      <div class="container">
        <div class="row d-flex align-items-center">
          <div class="col">
            <h1 class="display-4">
              <span> Club de Juegos Rosario </span>
            </h1>
            <p class="lead">Un lugar donde disfrutar de los mejores juegos de mesa modernos.</p>
            <a class="btn btn-primary btn-lg" href="/collection" role="button">Explora nuestros juegos</a>
          </div>
        </div>
      </div>
    </header>

    <!-- Eventos -->
    <section id="events" class="py-4 bg">
      <div class="container">
        <div id="carouselExampleCaptions" class="carousel slide">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">

            <div class="carousel-item active">
              <img src="../assets/img/cej.jpg" class="d-block w-100" alt="...">
              <div class="carousel-caption">
                <h5>Eventos Anuales</h5>
                <p class="d-none d-md-block">Cultura en juego 2023</p>
              </div>
            </div>

            <div class="carousel-item">
              <img src="../assets/img/mensual.jpg" class="d-block w-100" alt="...">
              <div class="carousel-caption">
                <h5>Juntadas Mensuales</h5>
                <p></p>
              </div>
            </div>

            <div class="carousel-item">
              <img src="../assets/img/torneo.jpg" class="d-block w-100" alt="...">
              <div class="carousel-caption">
                <h5>Torneos</h5>
                <p class="d-none d-md-block">Torneo de Sagrada</p>
              </div>
            </div>

          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Anterior</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Siguiente</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Sección Sobre Nosotros -->
    <section id="about" class="py-5 bg">
      <div class="container">
        <h2 class="text-center mb-3">Sobre nosotros</h2>
        <p class="about">¡Bienvenido al Club de Juegos Rosario! Si eres un apasionado de los juegos de mesa modernos, este es tu lugar. Nos reunimos mensualmente en La Fortaleza de 19:00 a 04:00 para una noche épica llena de estrategia, diversión y camaradería. Además, te invitamos a nuestras juntadas semanales los miércoles en Invictus de 18:00 a 21:00, donde puedes descubrir nuevos juegos y hacer nuevos amigos. ¡Únete a nosotros y forma parte de la comunidad de jugadores más entusiasta de Rosario!</p>
      </div>
    </section>

    <!-- Sección Contacto -->
    <section id="contact" class="py-5 bg">
      <div class="container">
        <h2 class="text-center mb-4">Redes Sociales</h2>
        <div class="row justify-content-center">
          <a href="https://chat.whatsapp.com/J7888YH88f2IKlqye0q9XX" target="_blank" class="col-12 col-lg-3  d-flex justify-content-center" style="color: gray;">
            <i class="bi bi-whatsapp" style="font-size: 5rem;"></i>
          </a>
          <a href="https://www.instagram.com/clubdejuegos_rosario/" target="_blank" class="col-12 col-lg-3 d-flex justify-content-center" style="color: gray;">
            <i class="bi bi-instagram" style="font-size: 5rem;"></i>
          </a>
          <a href="https://www.facebook.com/ClubdeJuegosRosario" target="_blank" class="col-12 col-lg-3 d-flex justify-content-center" style="color: gray;">
            <i class="bi bi-facebook" style="font-size: 5rem;"></i>
          </a>
          <a href="https://twitter.com/ClubDeJuegosRos" target="_blank" class="col-12 col-lg-3 d-flex justify-content-center" style="color: gray;">
            <i class="bi bi-twitter" style="font-size: 5rem;"></i>
          </a>
        </div>
      </div>
    </section>
  </div>
</template>


<style scoped>
.carousel-item-body {
  height: 70vh;
}

img {
  height: 70vh;
  max-width: 100%;
  object-fit: contain;
}

.card {
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel-caption {
  background-color: rgba(0, 0, 0, 0.7);
  border-radius: 20px;
  padding: 1%;
  font-size: small;
}

.carousel-control-prev-icon, .carousel-control-next-icon {
  background-color: rgba(0, 0, 0, 0.7);
  border-radius: 10px;
}

.home {
  height: 80vh;
}

.btn {
  box-shadow: 0 0 100px rgba(0, 0, 0, 0.6);
}

i {
  text-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
  cursor: pointer;
}

i:hover {
  text-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
  color: var(--bs-primary-1);
}

h1, h2, h3, h4 {
  text-shadow: 0 0 20px rgba(0, 0, 0, 0.4);
}

h1, h2, h3, h4 {
  color: azure
}

.main-logo {
  height: 20vh;
  width: 20vh;
}

.about {
  text-align: justify;
}

.container {
  background-color: rgb(0, 0, 0, 0.7);
  box-shadow: 0 0 100px rgba(0, 0, 0, 0.9);
  color: azure;
  padding-left: 30px;
  padding-right: 30px;
  padding-top: 30px;
  padding-bottom: 30px;
  border-radius: 30px;
}
</style>