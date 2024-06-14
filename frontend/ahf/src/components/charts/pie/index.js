import * as React from 'react';
import { PieChart } from '@mui/x-charts/PieChart';

export default function AHfPie() {
  return (
    <PieChart
      series={[
        {
          data: [
            { id: 0, value: 80, label: 'Principa'},
            { id: 1, value: 9, label: 'series B' },
            { id: 2, value: 7, label: 'series C' },
            { id: 3, value: 5, label: 'series D' },
            
          ],
          innerRadius:50,
          outerRadius:80,
          paddingAngle:25
        },
      ]}
      width={282}
      height={166}
   
  
     

      
    />
  );
}