
import './style.css'

//Props: url_image, name, description
function CardMenu(props) {

  let url_image = "https://gordaolanches.com.br/wp-content/uploads/lanche-do-gordao-cosmopolis.png"

  return (
    <div className="c-card-menu_content">
      <div className="c-card-menu_left">
        <img src={props.url_image || url_image} alt="SEM IMAGEM" srcset="" />
      </div>
      <div className="c-card-menu_right">
        <h1>{props.name || "IgorFoods"}</h1>
        <p>{props.description || "Sed faucibus vitae mauris at tempor. Morbi finibus magna a arcu vehicula finibus."}</p>
      </div>

    </div>
  )
}

export default CardMenu;