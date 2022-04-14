
import logo from './logo.svg';

import './style.css'
import { Link } from 'react-router-dom';

//Props: color=[orange|black|''], title
function Menu() {
  return (
    <>
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
      <div class="login-area">
        <a href="">Entrar</a>
        <button>Cadastrar</button>
      </div>
    </>
  )
}

export default Menu;