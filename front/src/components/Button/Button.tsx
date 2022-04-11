import { ClassType, MouseEventHandler, ReactElement, ReactNode } from "react";
import { JsxElement } from "typescript";

import './style.css'

interface IProps {
  onClick?: MouseEventHandler
  value?: any,
  children: ReactNode,
  size?: number
}

function Button({ onClick, value, children, size = 1 }: IProps) {
  return (
    <button
      className='button'
      onClick={onClick}
      data-value={value}
      style={{ width: `calc((70.8px * ${size})` }}
    >
      {children}
    </button >
  )
}

export default Button;



// --------------------------------

// interface IProps {
//   onClick: Function
//   children: ReactNode,
//   isInput: Number
// }

// const Button = ({ children, onClick, isInput }: IProps) => {
//   const isNumber = (val: any) => {
//     if (!isNaN(val) || val === "C" || val === ".") {
//       return true;
//     }
//     return false;
//   };

//   const isEqual = (val: any) => {
//     if (val === "=") {
//       return true;
//     }
//     return false;
//   };

//   return (
//     <>
//       {isInput ? (
//         <div className="input">{children}</div>
//       ) : (
//         <div
//           className={`botao-wrapper botao ${isEqual(children) ? "btn-igual" : null} ${isNumber(children) ? null : "operacao"}`}
//           onClick={() => onClick(children)}
//         >
//           {children}
//         </div>
//       )}
//     </>
//   );
// };

// export default Button;