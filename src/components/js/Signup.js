import React, {useState} from 'react'
import axios from 'axios'
import '../css/Signup.css'
// import loginImg from '../images/IoT_Login.jpg'

export default function Login() {
  const [inputData, setInputData] = useState(
    {
      username:"", 
      first_name:"", 
      last_name:"", 
      email:"", 
      password:"", 
      password_confirm:"",
      is_active:true,
    }
  )
  
  const onChangeHandler = (e) => {
    const name = e.target.name
    const value = e.target.value
    setInputData({...inputData, [name]:value})
  }

  const handleSubmit = event => {
    event.preventDefault();
    if (inputData.password !== inputData.password_confirm){
      document.getElementsByName('password_confirm').setCustomValidity("Passwords Don't Match");
    }
    else{
      axios.post('http://localhost:5100/account/signup/', inputData
      ).then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  }

  return (
    <main className="main">
      <div className="signup__wrapper">
        <form className="content" onSubmit={handleSubmit}>
          
          <div className="buttons">
            <div className="close">
            </div>
            <div className="minimize">
            </div>
            <div className="zoom">
            </div>
          </div>

          <h2>SignUp Form</h2>
          <div className="signup__push__down">
            <label htmlFor="username"><b>Username</b></label>
            <input type="text" placeholder="Enter Username" name="username" value={inputData.username}  onChange={onChangeHandler} required></input>
          </div>

          <div className="signup__push__down">
            <label htmlFor="first_name"><b>First Name</b></label>
            <input type="text" placeholder="First Name" name="first_name"  value={inputData.first_name} onChange={onChangeHandler} required></input>
          </div>

          <div className="signup__push__down">
            <label htmlFor="last_name"><b>Last Name</b></label>
            <input type="text" placeholder="Last Name" name="last_name"  value={inputData.last_name} onChange={onChangeHandler} required></input>
          </div>
          
          <div className="signup__push__down">
            <label htmlFor="email"><b>Email</b></label>
            <input type="email" placeholder="email" name="email"  value={inputData.email} onChange={onChangeHandler} required></input>
          </div>

          <div className="signup__push__down">
            <label htmlFor="password"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="password"  value={inputData.password} onChange={onChangeHandler} required></input>
          </div>

          <div className="signup__push__down">
            <label htmlFor="password_confirm"><b>Confirm Password</b></label>
            <input id="password_confirm" type="password" placeholder="Confirm Password" name="password_confirm"  value={inputData.password_confirm} onChange={onChangeHandler} required></input>
          </div>

          <div className="signup__push__down">
            <button type="submit" >Log in</button>
            <button type="submit" >Sign Up</button>
          </div>

          <span className="psw">Forgot password</span>

        </form>
      </div>
    </main>
  )
}
