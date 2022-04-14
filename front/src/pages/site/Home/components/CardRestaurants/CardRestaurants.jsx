
import { Link } from "react-router-dom";
import Button from '../../../../../components/Button/Button';
import './style.css'

//Props: url_image, name, description
function CardMenu(props) {

  let url_image = props.url_image ?? "https://gordaolanches.com.br/wp-content/uploads/lanche-do-gordao-cosmopolis.png"

  return (
    <div className="c-restaurants-card_content">
      <div className="c-restaurants-card_left">
        <img src={props.url_image || url_image} alt="SEM IMAGEM" srcset="" />
      </div>
      <div className="c-restaurants-card_right">
        <h1>{props.name || "IgorFoods"}</h1>
        <p><b>Descrição:</b> <br /> {props.description || "Sem descrição."}</p>
        <p><b>Endereço:</b> <br /> {props.address || "Sem Endereço."}</p>
        <p><b>Responsável:</b> <br /> {props.responsible_name || "Sem responsável."}</p>

        <Link to={`/products/${props.id}`}>
          <Button title="Conhecer" />
        </Link>

      </div>
    </div>
  )
}

export default CardMenu;