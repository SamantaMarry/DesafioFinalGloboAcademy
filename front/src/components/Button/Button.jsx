
import './style.css'

//Props: color=[orange|black|''], title
function Button(props) {
  return (
    <button className={`btn ${props.color ? `btn_${props.color}` : ''}`}>
      {props.title || "Button"}
    </button >
  )
}

export default Button;