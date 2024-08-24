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
import { Link, useLocation } from 'react-router-dom';
import { Box, Stack, TableCell, TableRow } from '@mui/material';
import { Button } from 'flowbite-react';




const LoanDetail = () => {
  const [data, setData]                   = useState([])
  const [mlo, setMlo]                    = useState("") 
  const [parents, setParentMlo]          = useState(["John","Fuff"]) 
  const [total_mlo,setTotalMlo] = useState(0)
  const [_totalCommission,setTotalCommission] = useState(0)
  const [totalAhfCommission,setTotalAhfCommission] =  useState(0)
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const total = 0
  const loan_detail = searchParams.get('loan_detail');


  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/api/get_loan_detail/?loan_detail=${loan_detail}`)
          .then((response) => {
             setData(response.data)
             setTotalCommission(response.data[response.data.length-1].total_commission)
             setTotalAhfCommission(response.data[response.data.length-1].total_ahf_commission)
             setMlo(response.data[response.data.length-1].mlo)  
             setTotalMlo(response.data[response.data.length - 1].total_mlo)
             console.log("total_mlo=",response.data[response.data.length - 1].total_mlo);
          
          })
          .catch((error) => {
            console.log("error=",error);

          })

  },[_totalCommission,totalAhfCommission,total_mlo])



console.log("totalAhfCommission=",totalAhfCommission);
console.log("totalAhfCommission=",totalAhfCommission);
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
        Footer: () => (
          <Stack>
            Total Branch commission:<Box color="warning.main">$85,000</Box>
          </Stack>
        ),

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
        Footer: () => (
          <Stack>
            Total AHF commission:<Box color="warning.main">$21,450</Box>
          </Stack>
        ),
      
      },

      {
        accessorKey: 'recruiter_commission',
        header: 'Recruiter commission',
        Header: ({ column }) => (
          <div className='flex flex-col justify-center'>{
            ninth_columns.map((item) => {
              return <p>{item}</p>
            })
          }</div>
        ),
        size: 150,
        Footer: () => (
          <Stack>
            Total Recruiter commission:<Box color="warning.main">$42,500</Box>
          </Stack>
        ),
      
      },
     
    ],
    [],
  );

 
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
  const ninth_columns                      = ["Revenue commission"]

  const table = useMaterialReactTable({
    columns,
    data,
    enableFullScreenToggle: true,

  });
 


  return (

    <div className="flex flex-col justify-evenly">
      <AHFNavbar />
      <HorizontalLine />

        <TableRow>
          
          <TableCell>
          <div className='flex flex-row'>
            
          {parents.map((item, index) => (<a key={index} href='/detail/?id=30011'>{ "AHF" + "--> " + item }</a>))}
            </div>
          </TableCell>
       
        </TableRow>

        <TableRow>
          
          <TableCell>
            Recruited MLO:{total_mlo}
         
          </TableCell>
       
        </TableRow>

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
          enableStickyFooter 
        />

      </div>

    </div>
  );
};

export default LoanDetail;
