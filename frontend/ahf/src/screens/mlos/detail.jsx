import { List, Avatar } from "flowbite-react";
import { Table } from "flowbite-react";
import { useEffect, useMemo, useState } from "react";
import axios from "axios";
import { useLocation, useParams } from "react-router-dom";
import { useSelector } from "react-redux";
import Dot from "../../components/activity";
import { MaterialReactTable } from "material-react-table";
import { AHFNavbar } from "../../components/Navbar";

export function MloDetail() {
  const [isLoading, setIsLoading] = useState(true)
  const refreshToken = useSelector((state) => state.auth.refreshToken);
  console.log("refreshToken=",refreshToken)
  const [data,setData] = useState([])
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const id = searchParams.get('id');


  useEffect(()=> {
    const token = refreshToken
 
    const headers = {
      'Content-Type': 'application/json',
      'Authorization':`JWT ${token}`
    }

    axios.get(`http://127.0.0.1:8000/api/get_level_info/?node_id=${id}`,{headers})
         .then((data) => {
          setData(data.data)
          setIsLoading(false)
         })

  },[])
  const first_columns                      = ["MLO"]
  const second_columns                     = ["Level"]
  const thrid_columns                      = ["Loan"]
  const fourth_columns                     = ["Commission"]
  const columns = useMemo(
    () => [
      {
        accessorKey: 'mlo',
        header: 'MLO',
        Header: ({ column }) => (
          <div className='flex flex-col justify-center'>{
            first_columns.map((item) => {
              return <p>{item}</p>
            })
          }</div>
        ),
        size: 150,
      },

      {
        accessorKey: 'level',
        header: 'Level',
        Header: ({ column }) => (
          <div className='flex flex-col justify-center'>{
            second_columns.map((item) => {
              return <p>{item}</p>
            })
          }</div>
        ),
        size: 200,
      },
      {
        accessorKey: 'loan',
        header: 'Loan',
        Header: ({ column }) => (
          <div className='flex flex-col justify-center'>{
            thrid_columns.map((item) => {
              return <p>{item}</p>
            })
          }</div>
        ),
        size: 150,
      },
      {
        accessorKey: 'commission',
        header: 'Commission',
        Header: ({ column }) => (
          <div className='flex flex-col justify-center'>{
            fourth_columns.map((item) => {
              return <p>{item}</p>
            })
          }</div>
        ),
        size: 150,
      },


    ],
    [],
  );
  return (
    <div className="w-screen justify-center">
      <AHFNavbar />
     { data?
      <div className='lg:w-[1260px] sm:w-[646px] lg:mx-5'>
      <MaterialReactTable
        columns={columns}
        data={data}
        state={{ isLoading: isLoading }}
        muiCircularProgressProps={{
          color: 'secondary',
          thickness: 5,
          size: 55,
        }}
        muiSkeletonProps={{
          animation: 'pulse',
          height: 28,
        }}

      />
      </div>
          :
      <div className='h-screen w-screen flex flex-col justify-center text-center'>
            <Dot size={40} />
          </div>
}
      </div>
 
  );
}
