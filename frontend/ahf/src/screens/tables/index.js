import { useLayoutEffect, useMemo, useState } from 'react';
import {
  MaterialReactTable,
  useMaterialReactTable,
} from 'material-react-table';
import { AHFNavbar } from '../../components/Navbar';
import HorizontalLine from '../../components/Line';
import axios from 'axios';
import { useSelector } from 'react-redux';
import Header from '../../components/Header';



const AbovebreakpointTable = () => {
  const authToken = useSelector((state) => state.auth);
  const refreshToken = authToken.auth.refreshToken
  // const [data,setData] = useState([])
  const headers = {
    'Authorization': `JWT ${refreshToken}`, 
  };

  const first_columns = ["","Flat fee","Bps"]
  const second_columns = ["GCI","64,750.0 ","GCI"]
  const thrid_columns = ["AHF","$25,900.0","60%"]
  const fourth_columns = ["Branch","38850.0","40%"]


const data = [

];

for(let item of data) {
  data.push(
    {
      bps:item[0],  
      gci: item[1],
      ahf: item[2],
      branch: item[3]
    }
  )

}

  useLayoutEffect(() => {
      const url = "https://www.ahf.mortgage/api/"
      const headers = {
          Authorization: `JWT ${refreshToken}`,
        };
        
      axios.get(url, { headers })
          .then(response => {
              // setData(response.data)
              console.log(response.data)

          })
          .catch(error => {
            console.error(error); 
          });
      
  },[])

 
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

const table = useMaterialReactTable({
  columns,
  data,
  enableFullScreenToggle: true,

});

return (

  <div className="flex flex-col">
    <AHFNavbar />

    <HorizontalLine />

    <div className='lg:w-[1260px] sm:w-[646px] lg:mx-5'>
        <MaterialReactTable table={table} />
    </div>

  </div>
);
};

export default AbovebreakpointTable;
