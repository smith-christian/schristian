// import logo from './logo.svg';
import React, {useState} from 'react';
import './App.css';
// import io from "socket.io-client";
import Sidenav from './components/js/Side_nav';
import Dashboard from './components/js/Dashboard';
import Header from './components/js/Header';
import Login from './components/js/Login';
import SignUp from './components/js/Signup';
import Sio from './sio/Socketioclient';

// const sio = io("http://192.168.2.186:5100")


const header = {
  name: "Smith",
  NavTag: "DASHBOARD",
}

function App() {
  const [login, setlogin] = useState(true)
  // const [sdata, setsdata] = useState({})

  // useEffect(()=>{ 
  //   sio.on("my_message", (data) => {
  //     setsdata(JSON.parse(data))

  //   })
  // },[])

  // const i = Object.keys(sdata).map((v, i)=>{return <p key={i.toString()}>{v} : {sdata[v]}</p>})

  if (!login) {
    return (
      <div className="App">
        <style>{'body{background-color:#1e1e2e;}'}</style>
        <Header name={header.name} NavTag={header.NavTag}/>
        <div className='split'>
            <Sidenav/>
            <Dashboard val={<Sio/>}/>
        </div>
      </div>
    );
  }
  else {
    return (
      <div>
        <style>
          {
            'body{background-image: linear-gradient(151deg,rgb(34 128 247) 10%,#1e1e2e 50%,#1e1e2e 20%);}'
          }
        </style>
        {/* <Login/> */}
        <SignUp/>
      </div>
    );
  }
}

export default App;
