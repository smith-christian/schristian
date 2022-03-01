import React from 'react'
import Performance from './dashboard/Performance'
import '../css/Dashboard.css'


export default function Dashboard(props) {
  const {val} = props
  return (
    <div className='box'>
      <main className='center__chart'>
        <Performance val={val}/>
      </main>
    </div>
  )
}