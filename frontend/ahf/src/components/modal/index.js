
"use client";

import axios from "axios";
import { Button, Modal } from "flowbite-react";
import { useEffect, useState } from "react";

export function ModalBox({id,parent_id}) {
  const [openModal, setOpenModal] = useState(true);
  const [data, setData] = useState([]);


  useEffect(() => {
    async function getData() {
      try {
        const data =  await axios.get(`http://127.0.0.1:8000/api/get_node_info/?id=${id}&parent_id=${parent_id}`)
        const data_ = data.data
       setData(data_)

      } catch (error) {
        
      }
    }

    getData()
  },[])


     console.log("data=",data)
  return (
    <>
 
      <Modal dismissible show={openModal} onClose={() => setOpenModal(false)}>
        <Modal.Header>MLO:{data.mlo}</Modal.Header>
        <Modal.Body>
          <div className="space-y-6">
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
            MLO:{data.mlo} sponsor {data.number_childern} mlos
           </p>

           <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              {data.mlo} sponsored by {data.parent}
           </p>
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
            {data.mlo} is on level 1 from  {data.parent}

            </p>
          </div>
        </Modal.Body>
  
      </Modal>
    </>
  );
}
