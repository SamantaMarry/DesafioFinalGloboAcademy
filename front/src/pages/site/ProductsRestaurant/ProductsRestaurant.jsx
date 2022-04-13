import { PageMainSite } from "../../../components/PageMainSite"
// import { CardMenu } from "./components/CardMenu"

import './style.css'

export default function ProductsRestaurant() {
  return (
    <>
      <PageMainSite>
        <div className="c-site-page-products-restaurant" style={{ color: 'white' }}>
          <h1>Produtos</h1>
          <ul className='c-table-list'>
            <li className='c-table-list-item'>row 1</li>
            <li className='c-table-list-item'>row 2</li>
            <li className='c-table-list-item'>row 3</li>
          </ul>
        </div>
      </PageMainSite>
      {/* <CardMenu /> */}
    </>
  )
}