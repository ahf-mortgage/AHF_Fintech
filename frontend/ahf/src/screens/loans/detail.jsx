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



const LoanDetail = () => {

  const columns = useMemo(
    () => [
      {
        accessorKey: 'file_reference',
        header: 'File reference',
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
        accessorKey: 'loan_amount',
        header: 'Loan amount',
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
        accessorKey: 'date_funded',
        header: 'Date funded',
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
        accessorKey: 'bps',
        header: 'BPS',
        Header: ({ column }) => (
          <div className='flex flex-col justify-center'>{
            fourth_columns.map((item) => {
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
            fifth_columns.map((item) => {
              return <p>{item}</p>
            })
          }</div>
        ),
        size: 150,
      },

      {
        accessorKey: 'split',
        header: 'Split',
        Header: ({ column }) => (
          <div className='flex flex-col justify-center'>{
            sixth_columns.map((item) => {
              return <p>{item}</p>
            })
          }</div>
        ),
        size: 150,
      },


      {
        accessorKey: 'ahf_commission',
        header: 'AHF Loan',
        Header: ({ column }) => (
          <div className='flex flex-col justify-center'>{
            seventh_columns.map((item) => {
              return <p>{item}</p>
            })
          }</div>
        ),
        size: 150,
      },


      {
        accessorKey: 'branch_commission',
        header: 'Branch commission',
        Header: ({ column }) => (
          <div className='flex flex-col justify-center'>{
            eight_columns.map((item) => {
              return <p>{item}</p>
            })
          }</div>
        ),
        size: 150,
      },
     
    ],
    [],
  );

  const [data, setData]                    = useState([])
  const [construct_data, setConstructData] = useState([])
  const [bps, setBps]                      = useState(0)
  const first_columns                      = ["File reference"]
  const second_columns                     = ["Loan amount"]
  const thrid_columns                      = ["Date funded"]
  const fourth_columns                     = ["BPS"]
  const fifth_columns                      = ["GCI"]
  const sixth_columns                      = ["Split"]
  const seventh_columns                    = ["Branch commission"]
  const eight_columns                      = ["AHF commission"]

  const table = useMaterialReactTable({
    columns,
    data,
    enableFullScreenToggle: true,

  });

  useEffect(() => {
    axios.get(" http://127.0.0.1:8000/api/get_level_info/?node_id=30011")
          .then((response) => {
             setData(response.data)
          })
          .catch((error) => {
            console.log("error=",error);

          })

  },[])


  return (

    <div className="flex flex-col justify-evenly">
      <AHFNavbar />

      <HorizontalLine />

      <div className='lg:w-[1260px] sm:w-[646px] lg:mx-5'>
        <MaterialReactTable
          columns={columns}
          data={data}
          state={{ isLoading: false }}
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

export default LoanDetail;
