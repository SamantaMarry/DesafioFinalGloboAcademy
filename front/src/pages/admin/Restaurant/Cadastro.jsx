import { PageMainSite } from "../../../components/PageMainSite"
import { CardContent } from "../../../components/CardContent"

import './style.css'

export default function Restaurant() {
  return (
    <>
      <PageMainSite useFooter={false}>
        <div className="c-admin-page-restaurant-cadastro">
          <CardContent title="Restaurante">
            <div className="c-card-content_left">
              <input type="text" name='name' />
              <textarea name="description" rows="5" cols="30"></textarea>
            </div>
            <div className="c-card-content_right">

              <input type="text" name='address' />
              <input type="text" name='url_image' />
              <input type="text" name='responsible_name' />
            </div>
          </CardContent>
        </div>
      </PageMainSite>
    </>
  )
}