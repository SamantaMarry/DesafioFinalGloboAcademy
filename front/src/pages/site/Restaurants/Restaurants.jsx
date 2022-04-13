import { PageMainSite } from "../../../components/PageMainSite"

import './style.css'

export default function Restaurants() {
  return (
    <>
      <PageMainSite>
        <div className="c-site-page-restaurants" style={{ color: 'white' }}>
          <h1>Restaurants</h1>
          <ul className='c-table-list'>
            <li className='c-table-list-item'>row 1</li>
            <li className='c-table-list-item'>row 2</li>
            <li className='c-table-list-item'>row 3</li>
          </ul>
        </div>
      </PageMainSite>
    </>
  )
}