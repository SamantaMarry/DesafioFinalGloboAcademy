
import logo from './logo.svg';

import './style.css'
import { Link } from 'react-router-dom';

//Props: color=[orange|black|''], title
function Menu() {
  return (
    <>


      <div class="logo-links">
        <Link to={'/'}>
          <div id="logo">
            <img src={logo} />
          </div>
        </Link>

        <nav class="menu">
          <div class="links-menu">
            <ul>
              <Link to={'/'}>
                <li><a href="">Restaurantes</a></li>
              </Link>
              <Link to={'/admin/restaurant/cadastro'}>
                <li><a href=""> Cadastre seu Restaurante</a></li>
              </Link>
              <Link to={'/admin/product/cadastro'}>
                <li><a href="">Cadastre seu Produto</a></li>
              </Link>
            </ul>
          </div>
        </nav>
      </div>

      {/*
            <nav class="menu">
              <div class="links-menu">
                <ul>
                  <li><a href="">Restaurantes</a></li>
                  <li><a href="">Trabalhe conosco</a></li>
                  <li><a href="">Entregas</a></li>
                </ul>
              </div>        
            </nav>
            */}

    <div class="login">
      <div class="login-area">
        <a href="">Entrar</a>
        <button>Cadastrar</button>
      </div>
    </div>
    </>
  )
}
export default Menu;