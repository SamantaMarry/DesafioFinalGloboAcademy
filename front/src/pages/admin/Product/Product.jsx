import { CardContent } from "../../../components/CardContent"
import { Button } from "../../../components/Button"

import './style.css'

export default function Product() {
  return (
    <>
      <CardContent title="Cardápio">
        <div className="c-card-content_left">
          <input type="text" name='name' />
          <textarea name="description" rows="5" cols="30"></textarea>
        </div>
        <div className="c-card-content_right">
          <input type="text" name='url_image' />
          <input type="text" name='price' />
        </div>
      </CardContent>
      <Button color="orange" />
    </>
  )
}