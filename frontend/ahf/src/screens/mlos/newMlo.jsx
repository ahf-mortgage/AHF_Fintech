"use client";

import axios from "axios";
import { Button, Label, Select } from "flowbite-react";
import { useEffect, useState } from "react";
import { json, useNavigate } from "react-router-dom";

export function AddMlo({source_node}) {
    const [data, setData] = useState([]);
    const [target_node, setTargetNode] = useState("");
    const navigate     = useNavigate(); 

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/get-all-nodes/")
            .then((response) => setData(response.data))
            .catch((error) => console.log("error=", error));
    }, []);


    const config = {
        headers: {
          'Content-Type': 'application/json'
        }
      };
      const request = {
        source_node: source_node.original.mlo,
        target_node: target_node
      };
  
    const handleAddMlo = () => {
        axios.post("http://127.0.0.1:8000/api/get-all-nodes/",request,config)
        .then((response) =>  navigate("/graph"))
        .catch((error) => console.log("error=", error));
    }

    const handleSourceNode = (event) => {
        
        setTargetNode(event.target.value);
        console.log("target_node=",target_node);
    }
    return (
        <div className="max-w-md">
        <div className="mb-2 block">
          <Label htmlFor="mlos" value="Select New MLO" />
        </div>
  
        <Select
          id="mlos"
          value={target_node}
          onChange={handleSourceNode}
          required
        >
          <option value="">Select  MLO</option>
          {data.map((item) => (
            <option key={item.label} value={item.label}>
              {item.label}
            </option>
          ))}
        </Select>
        <br />
  
        <Button size="md" onClick={handleAddMlo}>Save</Button>
      </div>
    );
}