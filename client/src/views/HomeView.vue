<template>
  <div class="home">
    <!-- Encabezado -->
    <header id="inicio" class="jumbotron jumbotron-fluid text-center bg">
      <div class="container">
        <h1 class="display-4">Club de Juegos Rosario</h1>
        <!-- <img src="../assets/logo.png" alt="" class="main-logo"> -->
        <p class="lead">Un lugar donde disfrutar de los mejores juegos de mesa modernos.</p>
        <a class="btn btn-primary btn-lg" href="/collection" role="button">Explora nuestros juegos</a>
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
              <img src="https://culturaenjuego.ar/fotos/0_whatsappimage2023-09-30at8.47.02pm1.jpg" class="d-block w-100" alt="...">
              <div class="carousel-caption">
                <h5>Eventos Anuales</h5>
                <p class="d-none d-md-block">Cultura en juego 2023</p>
              </div>
              
            </div>
            <div class="carousel-item">
              <img src="https://scontent.fros9-1.fna.fbcdn.net/v/t39.30808-6/393170089_848219230645938_1382657175920257997_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeGn-E6r4xWiM8C8l9e5QsFfYqmZDg-w_y5iqZkOD7D_LocWTnpViYvPhSi4lUiGSEgHpTn1ZdStuPqiOrEX-itL&_nc_ohc=gjL-e-eMrtYAb4cwEln&_nc_ht=scontent.fros9-1.fna&oh=00_AfCqSpDJcZivcIQik8S8iwuqGxYpQchfx6fvsgSp7DpB2w&oe=6623435D" class="d-block w-100" alt="...">
              <div class="carousel-caption">
                <h5>Torneos</h5>
                <p class="d-none d-md-block">Torneo de Catan</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://scontent.fros9-1.fna.fbcdn.net/v/t39.30808-6/432942445_929797639154763_5953871606034285322_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeHtrTqAQrlfdDTeXI8FjExz0klgzPB1XQLSSWDM8HVdAr5Nr0QFLUWGoDMfvcVaSlMzTv0zK570XW-zKuWNHY5F&_nc_ohc=oFuhpjxyclYAb6bvkre&_nc_oc=AdgovMvMYjKrg2rhdVbk4JwxtaVUIeUBWHF18pfl78kvZIzKt5mNwd_NYYoVh4qASuY&_nc_ht=scontent.fros9-1.fna&oh=00_AfDSPi0DRFGGIVBGnRKW0KR5zN6IHdfQzW04i3EW1LASVA&oe=6623496E" class="d-block w-100" alt="...">
              <div class="carousel-caption">
                <h5>Juntadas Mensuales</h5>
                <p></p>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Sección Sobre Nosotros -->
    <section id="about" class="py-5 bg">
      <div class="container">
        <h2 class="text-center mb-3">Sobre nosotros</h2>
        <p class="about">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ipsa nihil nemo dolores quod voluptatem odit necessitatibus temporibus nam autem beatae labore, accusantium pariatur vel saepe recusandae. Adipisci eius natus quidem qui, optio tempora at enim? Eveniet ut omnis porro perspiciatis. Molestiae saepe, quae quis quisquam pariatur nemo tempore ab excepturi animi consectetur ullam tempora blanditiis vel architecto nihil in non vitae doloribus iste, nobis possimus autem laboriosam? Culpa molestias ratione iste, esse excepturi quaerat illum! Ex, quod. Nostrum, aperiam? Quod repudiandae, nobis optio asperiores earum fuga nemo autem? Quas magnam velit dicta repellendus fuga culpa nostrum facere assumenda non recusandae?.</p>
      </div>
    </section>

    <!-- Sección Contacto -->
    <section id="contact" class="py-5 bg">
      <div class="container">
        <!-- <h2 class="text-center mb-4">Redes Sociales</h2> -->
        <div class="row justify-content-center">
          <!-- <a href="#" target="_blank" class="col d-flex justify-content-center">
            <i class="bi bi-whatsapp" style="font-size: 5rem;"></i>
          </a> -->
          <a href="https://www.instagram.com/clubdejuegos_rosario/" target="_blank" class="col d-flex justify-content-center" style="color: var(--bs-body-color);">
            <i class="bi bi-instagram" style="font-size: 5rem;"></i>
          </a>
          <a href="https://www.facebook.com/ClubdeJuegosRosario" target="_blank" class="col d-flex justify-content-center" style="color: var(--bs-body-color);">
            <i class="bi bi-facebook" style="font-size: 5rem;"></i>
          </a>
          <a href="https://discord.com/invite/DvnqgeHB" target="_blank" class="col d-flex justify-content-center" style="color: var(--bs-body-color);">
            <i class="bi bi-discord" style="font-size: 5rem;"></i>
          </a>
          <a href="https://twitter.com/ClubDeJuegosRos" target="_blank" class="col d-flex justify-content-center" style="color: var(--bs-body-color);">
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

.carousel {
  box-shadow: 0 0 100px rgba(0, 0, 0, 0.6);
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
  color: rgba(15, 15, 15, 0.9);
}

.main-logo {
  height: 20vh;
  width: 20vh;
}

.about {
  text-align: justify;
}
</style>