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
              <label htmlFor="">Nome do produto</label>
              <input type="text" name='name' placeholder="Digite o nome do produto"/>
              <label htmlFor="">Descrição</label>
              <textarea name="description" rows="5" cols="30" placeholder="Descrição"></textarea>
            </div>
            <div className="c-card-content_right">
              <label htmlFor="">Imagem do produto</label>
              <input type="text" name='url_image' placeholder="Cole a URL da imagem aqui" />
              <label htmlFor="">Preço</label>
              <input type="text" name='price' placeholder="Digite o preço do produto" />
              <Button title="Salvar">Salvar</Button>
            </div>
          </CardContent>
        </div>
      </PageMainSite>
    </>
  )
}