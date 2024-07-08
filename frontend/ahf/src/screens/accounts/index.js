
"use client";
import { Button, Label, TextInput,Card,Checkbox,ListGroup} from "flowbite-react";
import { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import "./index.css"
import { setRefreshToken } from "../../context/action";
import { useDispatch, useSelector } from "react-redux";
import HorizontalLine from '../../components/Line';
import { GoogleOAuthProvider } from '@react-oauth/google';
import { FaGoogle,FaEye ,FaEyeSlash } from "react-icons/fa";
import { Dots } from "react-activity";
import Dot from "../../components/activity";


function LoginPage({ navigation }) {
  const authToken = useSelector((state) => state.auth);
  
  const [username, setUsername]        = useState("John")
  const [password, setPassword]        = useState("")
  const [showPassword,setShowPassword] = useState(false)
  const [loading,setLoading]           = useState(false)
  const [errorMsg,setErrorMsg]         = useState("")
  const [errorKey,setErrorKey]         = useState("")
  const navigate                       = useNavigate();   
  const dispatch                       = useDispatch();
                      


  function toggleShowPassword() {
    setShowPassword(!showPassword)
  }

  function login(event) {
    event.preventDefault()
    setLoading(true)
    const config = {
      headers: {
        'Content-Type': 'application/json'
      }
    };

    const data = {
      username: username,
      password: password
    };

    axios.post('http://127.0.0.1:8000/auth/jwt/create/', data, config)
      .then(response => {
        console.log(response.status)
     
        if(response.status == 200) {
          const token = response.data.access
          dispatch(setRefreshToken(token));
          navigate("/dashboard")
          setLoading(false)
        }
        else {
          navigate("/")
        }
    
      })
      .catch(error => {
        console.log("error=",error)
        // const errors = Object.entries(error.response.data)
        // errors.filter(item => {
        //   setErrorKey(item[0])
        //   setErrorMsg(item[1])
        // })
        // setLoading(false)
      });
  }


  return (

    <div className="h-screen w-screen bg-[#F2F7FA]">
    <div className="flex justify-center items-center h-screen">

     <Card className="w-[546px] h-[550px] justify-center items-center">

      <p className="text-[#2A3135] text-[32px] font-['Roboto_Slab'] text-center">Sign into your account </p>
      <p className="text-red-500 font-['Roboto_Slab'] text-center">{errorKey} {errorMsg}</p>
  
      <form className="flex flex-col gap-4">
        <div>
          <div className="mb-2 block">
            <Label htmlFor="username" value="Username" />
          </div>
          <TextInput 
              id="username"
              type="text" 
              className="w-[369px] h-[38px]" placeholder="John" required
              value={username}
              onChange = {(event) => setUsername(event.target.value)}
                />
        </div>
        <div>
          <div className="mb-0 block">
            <Label htmlFor="password1" value="Password" />
          </div>
          <div>
            
          </div>
          <div className="">
              <TextInput 
                  id="password1"
                  className="w-[369px] h-[38px]" type={ showPassword ? 'text' : 'password' } required
                  value={password}
                  onChange = {(event) => setPassword(event.target.value)}
                  />
            {
              showPassword ? (
                <FaEyeSlash
                  className="absolute inset-y-[48%] right-[15%] lg:right-[36%] flex items-center cursor-pointer"
                  onClick={
                    () => toggleShowPassword()
                  }
                />
              ) : (
                <FaEye
                  className="absolute inset-y-[48%] right-[15%] lg:right-[36%] md:right-[10%] flex items-center cursor-pointer"
                  onClick={() => toggleShowPassword()}
                />
              )
            }
          </div>
        
        </div>
        <div className="flex items-center justify-end gap-2">
          <ListGroup.Item href="/resetpassword" className="list-none text-[12px] text-[#194863] mt-[0px] h-[50px] text-center justify-center">
            Forgot password ?
          </ListGroup.Item>

        </div>
        {
        loading?
        <div className="w-[369px] h-[38px] text-center">
          <Dot  />
        </div>
            :
        <Button 
          type="submit"
          className="w-[369px] h-[38px] text-center"
          onClick = {(event) => login(event)}
          >
          Sign in
        </Button>
          
        }

        <div className="flex items-center">
          <HorizontalLine width={125} color={'#FFFFFF'} className="" />
          <p className="mx-4 w-[120px] h-[45px] text-center">Or continue with</p>
          <HorizontalLine width={95} color={'#FFFFFF'} className="" />
        </div>

      </form>



      <div className="flex justify-between">
        
        <GoogleOAuthProvider clientId="<your_client_id>">
          Sign in with google
        </GoogleOAuthProvider>
        <FaGoogle />
      </div>
    </Card>
  </div>
  </div>
  );

}

export default LoginPage
