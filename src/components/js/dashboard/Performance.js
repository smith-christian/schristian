import React from 'react'
import '../../css/Performance.css'

export default function Performance(props) {

  const btnVal = ["Temperature","Battery","Other",]
  const {val} = props


  const button_activation_handler = (btn, e) => {
  }
  
  const buttons = btnVal.map((btn)=>{ return <button key={btn.toString()} className="performance__button" onClick={(e)=>button_activation_handler(btn, e)}>{btn}</button>})

  return (
    <div  className='performance__chart'>
        <div className='__flex'>
            <p>Performance</p>
            <div>
              {buttons}
            </div>
        </div>
        <div>{val}</div>
    </div>
  )
}