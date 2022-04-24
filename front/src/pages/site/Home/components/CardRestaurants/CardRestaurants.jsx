
import { Link } from "react-router-dom";
import Button from '../../../../../components/Button/Button';
import './style.css'

//Props: url_image, name, description
function CardMenu(props) {

  const name = props.data.name ?? "Sem Nome"
  const url_image = props.data.url_image ?? "https://gordaolanches.com.br/wp-content/uploads/lanche-do-gordao-cosmopolis.png"
  const address = props.data.address ?? "Sem Endereço"
  const description = props.data.description ?? "Sem Descrição"
  const responsible_name = props.data.responsible_name ?? "Sem Responsável"

  return (
    <div className="c-restaurants-card_content">
      <div className="c-restaurants-card_left">
        <img src={url_image} alt="SEM IMAGEM" />
      </div>
      <div className="c-restaurants-card_right">
        <h1>{name}</h1>
        <p><b>Descrição:</b> <br /> {address}</p>
        <p><b>Endereço:</b> <br /> {description}</p>
        <p><b>Responsável:</b> <br /> {responsible_name}</p>

        <Link to={`/products/${props.data.id}`}>
          <Button title="Conhecer" />
        </Link>

      </div>
    </div>
  )
}

export default CardMenu;