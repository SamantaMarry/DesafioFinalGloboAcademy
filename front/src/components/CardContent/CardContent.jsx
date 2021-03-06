
import './style.css'
import botao from './botao.svg';

//Props: title, children
function CardContent(props) {
  return (
    <div className="c-card-content_content">
      <header className="c-card-content_header">
        <h1>{props.title || "Title"}</h1>
      </header>
      <div className="c-card-content_main">
        {props.children}
      </div>
      <footer className="c-card-content_footer">
      </footer>
    </div>
  )
}

export default CardContent;