
import logo from './logo.svg';

import './style.css'
import { Link } from 'react-router-dom';

//Props: color=[orange|black|''], title
function Menu() {
  return (
    <>
      <div className="logo-links">
        <Link to={'/'}>
          <div id="logo">
            <img src={logo} />
          </div>
        </Link>

        <nav className="menu">
          <div className="links-menu">
            <ul>
              <li><Link to={'/'}>Restaurantes</Link></li>
              <li> <Link to={'/admin/restaurant/cadastro'}>Cadastre seu Restaurante </Link></li>
              <li><Link to={'/admin/product/cadastro'}>Cadastre seu Produto </Link></li>
            </ul>
          </div>
        </nav>
      </div>
      <div className="login">
        <div className="login-area">
          <a href="">Entrar</a>
          <button>Cadastrar</button>
        </div>
      </div>
    </>
  )
}
export default Menu;