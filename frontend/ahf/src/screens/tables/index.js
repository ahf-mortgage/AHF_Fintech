import { useLayoutEffect, useMemo, useState } from 'react';
import {
  MaterialReactTable,
  useMaterialReactTable,
} from 'material-react-table';
import { AHFNavbar } from '../../components/Navbar';
import HorizontalLine from '../../components/Line';
import axios from 'axios';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';





const data = [
  {
    name:'John',  
    address: '261 Erdman Ford',
    city: 'East Daphne',
    state: 'Kentucky',
  },
  {
    name: 'Jane', 
    address: '769 Dominic Grove',
    city: 'Columbus',
    state: 'Ohio',
  },
  {
    name: 'Joe',
    address: '566 Brakus Inlet',
    city: 'South Linda',
    state: 'West Virginia',
  },
  {
    name:  'Kevin',
    address: '722 Emie Stream',
    city: 'Lincoln',
    state: 'Nebraska',
  },
  {
    name: 'Joshua', 
    address: '32188 Larkin Turnpike',
    city: 'Charleston',
    state: 'South Carolina',
  },
];

const AbovebreakpointTable = () => {
  const authToken = useSelector((state) => state.auth);
  const refreshToken = authToken.auth.refreshToken
  const datum = []
  const headers = {
    'Authorization': `JWT ${refreshToken}`, 
  };

  useLayoutEffect(() => {
      const url = "https://www.ahf.mortgage/api/"
      const headers = {
          Authorization: `JWT ${refreshToken}`,
        };
        
      axios.get(url, { headers })
          .then(response => {
     
              console.log(response.data)
              const list_of_data  = response.data
              for(let data of list_of_data) {
                datum.push(data)

              }
              console.log("datum=",datum)
 
          })
          .catch(error => {
            console.error(error); 
          });
      
  },[])

 
const columns = useMemo(
  () => [
    {
      accessorKey: 'name',
      header: ['Name', 'First Name',"Last name"],
      size: 150,
    },
   
    {
      accessorKey: 'address',
      header: 'Address',
      size: 200,
    },
    {
      accessorKey: 'city',
      header: 'City',
      size: 150,
    },
    {
      accessorKey: 'state',
      header: ['State',"AHF"],
      Header: ({ column }) => (
        <i style={{ color: 'red'}}>
          {column.columnDef.header} 
        
          </i> 
      ), 

      Cell: ({ renderedCellValue, row }) => (
        <Link to={`/profile/${row.original.username}`}>
          {renderedCellValue}
        </Link>
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
        <MaterialReactTable table={table}  />
    </div>

  </div>
);
};

export default AbovebreakpointTable;
