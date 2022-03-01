import React from 'react'
import '../css/Header.css'

export default function Header(props) {
    const {name, NavTag} = props
  return (
      <header>
          <h3>{NavTag}</h3>
          <div>
              <button>Search</button>
              <button>Coming Soon</button>
              <button>{name}</button>
          </div>
      </header>
      
  )
}
