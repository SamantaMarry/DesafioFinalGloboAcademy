import './home.css';
import logo from './logo.svg';
import background from './background.svg';

export default function Home() {
  return (
    <>
      <body style={{ backgroundImage: `url(${background})` }}>
        <header>
          <div id="logo">
            <img src={logo}/>
          </div>
          <div class="menu">
            <div class="links-menu">
              <ul>
                <li><a href="">Restaurantes</a></li>
                <li><a href="">Trabalhe conosco</a></li>
                <li><a href="">Entregas</a></li>
              </ul>
            </div>
          </div>
          <div class="login-area">
            <a href="">Entrar</a>
            <button>Cadastrar</button>
          </div>
        </header>

        <main>
          <article id="main-content">
            <section id="search-box">
              <h2>Escolha a sua<br />
               comida favorita.</h2>
              <input type="text" placeholder="Ex: Tom, The Italian" />
              <button>buscar</button>
            </section>

            <section class="catalogs" id="catalog1">
              <h3>Venha para o Jason's Food!</h3>
              <p>Acelere o seu negócio</p>
              <ul>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
              </ul>
            </section>
            <section class="catalogs" id="catalog2">
            <p>Acelere o seu negócio</p>
              <ul>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
              </ul>
            </section>
            <section class="food-style">
              <h4>Comida para todo mundo!</h4>
              </section>
          </article>
        </main>
        <footer></footer>
      </body>
</>
  )

}