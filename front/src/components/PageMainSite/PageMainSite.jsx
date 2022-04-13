// import Head from "./components/Head";
import HeaderMain from "./components/HeaderMain";
import FooterMain from "./components/FooterMain";

import { Menu } from '../Menu';

import './style.css'
import background from './background.svg';

export default function PageMain(props) {

  const useHeader = props.useHeader ?? true
  const useMenu = props.useMenu ?? true
  const useFooter = props.useFooter ?? true

  // console.log(useHeader, useMenu, useFooter);

  return (
    <>
      <div className="c-page-main-site_content" style={{ backgroundImage: `url(${background})` }} >
        {(useHeader) ?
          <HeaderMain> {(useMenu) ? <Menu /> : ""} </HeaderMain>
          : ""
        }
        {props.children}
        {(useFooter) ? <FooterMain /> : ""}
      </div>
    </>
  )
}