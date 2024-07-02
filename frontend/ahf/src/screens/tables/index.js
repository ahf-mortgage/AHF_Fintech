import { useEffect, useLayoutEffect, useMemo, useState } from 'react';
import {
  MaterialReactTable,
  useMaterialReactTable,
  useMRT_Rows
} from 'material-react-table';
import { AHFNavbar } from '../../components/Navbar';
import HorizontalLine from '../../components/Line';
import axios from 'axios';
import { useSelector } from 'react-redux';
import Header from '../../components/Header';
import { faL } from '@fortawesome/free-solid-svg-icons';



const AbovebreakpointTable = () => {
  const authToken = useSelector((state) => state.auth);
  const refreshToken = authToken.auth.refreshToken
  const [isLoading, setIsLoading] = useState(true)

  const [data, setData]                    = useState([])
  const [construct_data, setConstructData] = useState([])
  const [bps, setBps]                      = useState(0)
  const first_columns                      = ["", "Flat fee", "Bps"]
  const second_columns                     = ["GCI", "64,750.0 ", "GCI"]
  const thrid_columns                      = ["AHF", "$25,900.0", "60%"]
  const fourth_columns                     = ["Branch", "38850.0", "40%"]




  useEffect(() => {
    const new_data = []

    const url = "https://www.ahf.mortgage/api/"
    const headers = {
      Authorization: `JWT ${refreshToken}`,
    };

    axios.get(url, { headers })
      .then(response => {
        const data = response.data
        for (let d of data) {
          new_data.push({
            bps: d[0],
            gci: d[1],
            ahf: d[2],
            branch: d[3]
          })
        }
        setData(new_data)
        setIsLoading(false)

      })
      .catch(error => {
        console.error(error);
      });

  }, [])



  const columns = useMemo(
    () => [
      {
        accessorKey: 'bps',
        header: 'BPS',
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
        accessorKey: 'gci',
        header: 'GCI',
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
        accessorKey: 'ahf',
        header: '40.00%',
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
        accessorKey: 'branch',
        header: '60.00%',
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
  console.log("construct data =", data)


  const table = useMaterialReactTable({
    columns,
    data,
    enableFullScreenToggle: true,

  });

  return (

    <div className="flex flex-col justify-evenly">
      <AHFNavbar />

      <HorizontalLine />

      <div className='lg:w-[1260px] sm:w-[646px] lg:mx-5'>
        <MaterialReactTable
          // table={table}
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

    </div>
  );
};

export default AbovebreakpointTable;
