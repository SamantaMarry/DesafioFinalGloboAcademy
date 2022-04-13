import './style.css';
import catalog from './catalog.svg';

import { PageMainSite } from "../../../components/PageMainSite"

export default function Home() {
  return (
    <>
      <PageMainSite>
        <main>
          <article id="main-content">

            <section id="search-box">
              <h2>Escolha a sua<br />
                comida favorita.</h2>
              <input type="text" placeholder="Ex: Tom, The Italian" />
              <button>buscar</button>
            </section>

            <section class="food-style">
              <h4>Comida para todo <br />
                gosto!</h4>
              <img src={catalog} />
            </section>


            {/*<section class="catalogs" id="catalog1">
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
            </section>*/}

          </article>
        </main>
      </PageMainSite>
    </>
  )

}