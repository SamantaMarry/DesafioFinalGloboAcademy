import { PageMainSite } from "../../../components/PageMainSite"
import { CardContent } from "../../../components/CardContent"
// import { Button } from "../../../components/Button"
// <Button color="orange" />

import './style.css'
import Button from './../../../components/Button/Button';

export default function Product() {
  return (
    <>
      <PageMainSite useFooter={false}>
        <div className="c-admin-page-products-cadastro">
          <CardContent title="Cardápio">
            <div className="c-card-content_left">
              <input type="text" name='name' />
              <textarea name="description" rows="5" cols="30"></textarea>
            </div>
            <div className="c-card-content_right">
              <input type="text" name='url_image' />
              <input type="text" name='price' />
              <Button title="Salvar">Salvar</Button>
            </div>
          </CardContent>
        </div>
      </PageMainSite>
    </>
  )
}