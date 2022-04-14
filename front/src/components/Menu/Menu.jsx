
import logo from './logo.svg';

import './style.css'

//Props: color=[orange|black|''], title
function Menu() {
  return (
    <>
      <div id="logo-links">
        <div id="logo">
          <img src={logo} />
        </div>
        <nav class="menu">
          <div class="links-menu">
            <ul>
              <li><a href="">Restaurantes</a></li>
              <li><a href="">Trabalhe conosco</a></li>
              <li><a href="">Entregas</a></li>
            </ul>
          </div>        
      </nav>
      </div>
      <div class="login-area">
        <a href="">Entrar</a>
        <button>Cadastrar</button>
      </div>
    </>
  )
}

export default Menu;