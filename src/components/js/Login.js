import React, {useState} from 'react'
import axios from 'axios'
import '../css/Login.css'
// import loginImg from '../images/IoT_Login.jpg'

export default function Login() {
  const [inputData, setInputData] = useState({username:"", password:""})
  const [n, setN] = useState("")
  
  const onChangeHandler = (e) => {
    const name = e.target.name
    const value = e.target.value
    setInputData({...inputData, [name]:value})
  }

  const handleSubmit = event => {
    event.preventDefault();

    axios.post('http://localhost:5100/gettoken/', inputData
    ).then(function (response) {
      setN(JSON.parse(response.config.data).username);
      // console.log(response.data.refresh);

      axios.get('http://localhost:5100/account/user/', {headers: { 
        'Authorization': `Bearer ${response.data.access}`,
      }})
      .then(function (response) {
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
    })
    .catch(function (error) {
      console.log(error);
    });
   
  }

  return (
    <main className="main">
      <div className="wrapper">
        <form className="content" onSubmit={handleSubmit}>
          
          <div className="buttons">
            <div className="close">
            </div>
            <div className="minimize">
            </div>
            <div className="zoom">
            </div>
          </div>

          <h2>Login Form</h2>
          <div>{n}</div>
          <div className="push__down">
            <label htmlFor="username"><b>Username</b></label>
            <input type="text" placeholder="Enter Username" name="username"  onChange={onChangeHandler} required></input>
          </div>

          <div className="push__down">
            <label htmlFor="password"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="password" onChange={onChangeHandler} required></input>
          </div>

          <div className="push__down">
            <button type="submit" >Log in</button>
            <button type="submit" >Sign Up</button>
          </div>

          <span className="psw">Forgot password</span>

        </form>
      </div>
    </main>
  )
}
