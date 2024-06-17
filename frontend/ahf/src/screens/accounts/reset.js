
"use client";
import { Button, Label, TextInput, Card, Checkbox, ListGroup } from "flowbite-react";
import { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import "./index.css"
import { setRefreshToken } from "../../context/action";
import { useDispatch, useSelector } from "react-redux";
import HorizontalLine from '../../components/Line';
import { GoogleOAuthProvider } from '@react-oauth/google';
import { FaGoogle, FaEye, FaEyeSlash } from "react-icons/fa";
import { Dots } from "react-activity";
import Dot from "../../components/activity";






function ResetPassword({ navigation }) {
  const refreshToken = useSelector((state) => state.auth.refreshToken);
  const [username, setUsername] = useState("MLO")
  const [password, setPassword] = useState("")
  const [showPassword, setShowPassword] = useState(false)
  const [loading, setLoading] = useState(false)
  const [errorMsg, setErrorMsg] = useState("")
  const [errorKey, setErrorKey] = useState("")
  const navigate = useNavigate();
  const dispatch = useDispatch();


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

    axios.post('https://www.ahf.mortgage/auth/jwt/create/', data, config)
      .then(response => {
        const token = response.data.access
        dispatch(setRefreshToken(token));
        navigate("/dashboard")
        setLoading(false)
      })
      .catch(error => {

        const errors = Object.entries(error.response.data)
        errors.filter(item => {
          setErrorKey(item[0])
          setErrorMsg(item[1])
        })
        setLoading(false)
      });
  }


  return (

    <div className="h-screen w-screen bg-[#F2F7FA]">
      <div className="flex justify-center items-center h-screen">

        <Card className="w-[546px] h-[450px] justify-center items-center">
        <p className="text-[#2A3135] text-[32px] font-['Roboto_Slab'] text-center">Reset Password</p>
          <form className="flex flex-col gap-4">
            <div>
              <div className="mb-2 block">
                <Label htmlFor="email1" value="Email" />
              </div>
              <TextInput
                id="email1"
                type="email"
                className="w-[369px] h-[38px]" placeholder="John" required
                value={username}
                onChange={(event) => setUsername(event.target.value)}
              />
            </div>

            <Button 
          type="submit"
          className="w-[369px] h-[38px] mt-[47px] text-center bg-[#3290C5]"
          onClick = {(event) => login(event)}
          >
          Reset password
        </Button>
          </form>

        </Card>
      </div>
    </div>
  );

}

export default ResetPassword
