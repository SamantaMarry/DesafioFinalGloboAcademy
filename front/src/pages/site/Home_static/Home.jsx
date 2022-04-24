import './style.css';
import logo from './logo.svg';
import background from './background.svg';
import catalog from './catalog.svg';

export default function Home() {
  return (
    <>
      <body style={{ backgroundImage: `url(${background})` }}>
        <header>
          <div id="logo-links">
            <div id="logo">
              <img src={logo} />
            </div>
            <div className="menu">
              <div className="links-menu">
                <ul>
                  <li><a href="">Restaurantes</a></li>
                  <li><a href="">Trabalhe conosco</a></li>
                  <li><a href="">Entregas</a></li>
                </ul>
              </div>
            </div>
          </div>
          <div className="login-area">
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

            <section className="food-style">
              <h4>Comida para todo <br />
                gosto!</h4>
              <img src={catalog} />
            </section>


            {/*<section className="catalogs" id="catalog1">
              <h3>Venha para o Jason's Food!</h3>
              <p>Acelere o seu negócio</p>
              <ul>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
              </ul>
            </section>
            <section className="catalogs" id="catalog2">
              <p>Acelere o seu negócio</p>
              <ul>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
                <li><a href="#">Lorem Ipsum</a></li>
              </ul>
            </section>*/}

          </article>
        </main>
        <footer>
          <section className="places">
            <p>onde estamos</p>
            <ul>
              <li><a href="#">recife</a></li>
              <li><a href="#">joão Pessoa</a></li>
              <li><a href="#">são paulo</a></li>
              <li><a href="#">rio de janeiro</a></li>
              <li><a href="#">belo horizonte</a></li>
              <li><a href="#">porto alegre</a></li>
            </ul>
          </section>
          <section className="contact">
            <p>contato</p>
            <ul>
              <li><a href="#">facebook.com/JasonsFood</a></li>
              <li><a href="#">twitter.com/JasonsFood</a></li>
              <li><a href="#">instagram.com/JasonsFood</a></li>
              <li><a href="#">contatojasonsfood@gmail.com</a></li>
              <li><a href="#">tel:  11 9 9999-9999</a></li>

            </ul>
          </section>
          <section className="jasons-food">
            <p>Jason's food</p>
            <ul>
              <li><a href="#">Políticas e termos</a></li>
              <li><a href="#">Sobre o Jason's Food</a></li>
            </ul>
          </section>
        </footer>
      </body>
    </>
  )

}