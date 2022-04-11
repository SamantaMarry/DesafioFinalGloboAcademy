import './styles.css'
import { ChangeEventHandler, useState } from 'react';

interface ScreenProps {
  historic?: Array<string>
  value?: any
  fnHandlerKeypress?: any
}

function Screen({ value, historic, fnHandlerKeypress }: ScreenProps) {
  return (
    <>
      <div className='screen'>
        <div className="historic">
          {historic?.map((expression, idx) => {
            return (
              <p key={idx}>{expression}</p>
            )
          })}
        </div>
        <div className="value">
          <input type="text" autoFocus readOnly={true} value={value} onKeyDown={fnHandlerKeypress} placeholder='0' />
          {/* <input type="text" autoFocus value={value} onChange={() => { }} onKeyDown={fnHandlerKeypress} placeholder='0' /> */}
        </div>
      </div>
    </>
  )
}

export default Screen;
