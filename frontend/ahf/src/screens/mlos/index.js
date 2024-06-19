import React, { useLayoutEffect, useState } from 'react';
import "./index.css"
import "./payment.css"
import "./summary.css"
import VideoComponent from '../../components/video';
import AHfPie from '../../components/charts/pie';
import { AHFNavbar } from '../../components/Navbar';
import HorizontalLine from '../../components/Line';
import { useSelector } from 'react-redux';
import axios from 'axios';
import CompPlan from '../../components/compplan';


function DashBoard() {
    const refreshToken = useSelector((state) => state.auth.refreshToken);


    useLayoutEffect(() => {
        const url = "https://www.ahf.mortgage/api/"
        const headers = {
            Authorization: `JWT ${refreshToken}`,
          };
          
        axios.get(url, { headers })
            .then(response => {

              setAboveData(response.data)
            })
            .catch(error => {
              console.error(error); 
            });
        
    },[])


  return (
    <div>
        <div class="container">

            {/* Navbar */}
                <div>
                    <AHFNavbar />
                </div>

            {/* HorizontalLine */}
                <div>
                    <HorizontalLine />
                </div>



        {/* comp plan table section */}
        <CompPlan />
  


        <div class="payement">
            <p className='payment-title'>Payment Breakdown</p>

           <div className='payment-bar'>
            <AHfPie margin={{bottom: "40px", left:  "40px", right:  "40px", top:  "400px" }}
             />
           </div>
           
        </div>

    

        <div class="loan">
    
          <h5>Loan Detail </h5>
           <div class="loan_txt1">
          <p>Home Value</p>
          <h3>$2000000.00</h3>
          <p>Monthly FHA Payment</p>
          <h3>$2000000.00</h3>
          <p>FHA Loan Amount</p>
          <h3>$2000000.00</h3> 
           </div>
           <div class="loan_txt2">
          <p>Base Loan Amount</p>
          <h3>$1930000.00</h3>
          <p>Down Payement</p>
          <h3>$1930000.00</h3>
          <p>Upgrount MIP:</p>
          <h3>$1930000.00</h3> 
           </div>
        </div>
        <div class="box1">
            <p>Monthly Mortage Payment</p>
            <h2>$1492.66</h2>

        </div>
        <div class="box2">
            <p>Your Debt to Income Ratio</p>
            <h2>29.85%/29.85%</h2>


        </div>
        <div class="box3">
            <p>Loan Amount</p>
            <h2>$1492.66</h2>

        </div>
        <div class="box4">
            <span>Allowable Debt to Income Ratio</span>
            <h2>46.9%/56.9%</h2>

        </div>
        <div class="box5">
            <div class="progress-container">
                 <h4>Progress</h4>
                <progress id="progress-bar" value="50" max="100"></progress>
                <input type="radio" name="progress" id="step1" checked />
              </div>
        </div>
        <div class="box6">

        </div>
        <div className="summery">
            <div className='vid-container'>
            <VideoComponent />

            </div>
          
            <title>Summary:</title>
                <p>
                Based on what you inpu
                    $1492.66 on a FHA Loas
                    Debt-to-Income Ratio l
                    allowable on this program type is 46.9%/ %6.9%.Please all
                    these numbers for accuracy with your loan Officer. The Mon
                    thly Debts Calculation is often where we see errors.
                </p>
        </div>
        
    </div>
    </div>
  );
}

export default DashBoard;