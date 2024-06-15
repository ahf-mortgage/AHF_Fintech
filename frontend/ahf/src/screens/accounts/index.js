
"use client";

import { Button, Checkbox, Label, TextInput } from "flowbite-react";
import { useState } from "react";

function LoginPage() {
  const [username,setUsername] = useState("MLO")
  const [password,setPassword] = useState("")
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
        <TextInput id="email1" type="pa" placeholder="ahf" required  value={username} onChange={(event) => setUsername(event.target.value)}/>
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
      <Button type="submit">Submit</Button>
    </form>
      </div>
  );
}

export default LoginPage
