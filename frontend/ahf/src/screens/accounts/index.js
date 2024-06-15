
"use client";

import { Button, Checkbox, Label, TextInput } from "flowbite-react";
import { useState } from "react";
import axios from 'axios';

function LoginPage() {
  const [username,setUsername] = useState("MLO")
  const [password,setPassword] = useState("")

  function login(event) {
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
        const token = response.data.token;
        console.log('Token:', token);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }


  return (
    
      <div style={{
        display:"flex",
        justifyContent:"center",
        alignItems:"center"
      }}>
            <form className="flex max-w-md flex-col gap-4">
      <div>
        <div className="mb-2 block">
          <Label htmlFor="email1" value="Username" />
        </div>
        <TextInput id="email1" type="text" placeholder="ahf" required  value={username} onChange={(event) => setUsername(event.target.value)}/>
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="password1" value="Your password" />
        </div>
        <TextInput id="password1" type="password" value={password}  onChange={(event) => setPassword(event.target.value)} required />
      </div>
      <div className="flex items-center gap-2">
        <Checkbox id="remember" />
        <Label htmlFor="remember">Remember me</Label>
      </div>
      <Button onClick = {(event) => login(event)}>Login</Button>
      
    </form>
      </div>
  );
}

export default LoginPage
