import React, {useState, useEffect} from 'react';
import io from "socket.io-client";

const sio = io("http://192.168.2.186:5100")

export default function Socketioclient() {

  const [sdata, setsdata] = useState({})

  useEffect(()=>{ 
    sio.on("my_message", (data) => {
      // console.log(data)
      setsdata(JSON.parse(data))

    })
  },[])

  const i = Object.keys(sdata).map((v, i)=>{return <p key={i.toString()}>{v} : {sdata[v]}</p>})

  return (
    <div  style={{overflow: 'overlay'}}>{i}</div>
  )
}
