import React from 'react';
import "./index.css"
import "./comp_plan.css"
import "./payment.css"
import "./summary.css"
import VideoComponent from '../../components/video';
import AHfPie from '../../components/charts/pie';
import { AHFNavbar } from '../../components/Navbar';
import HorizontalLine from '../../components/Line';


function DashBoard() {
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
        <div class="comp_plan">
            <div class="hero-content">
                
                <div class="comp_plan_title_container">
                    <p class="comp_plan_title">AHF Calculator</p>
                </div>

            {/* video components */}
            <div>
              <VideoComponent />
            </div>


            {/* complan navbar sectiin */}
            <div className='comp_plan_nav'>
                <nav>
                    <ul>
                        <li><a href="#">Conventional</a></li>
                        <li><a href="#">FHA</a></li>
                        <li><a href="#">VA</a></li>
                        <li><a href="#">USDA</a></li>
                        <li><a href="#">Jumbo</a></li>
            
                    </ul>
                </nav>
            </div>
            </div>


            <div className='section'>
                <div className='section-left'>
                <p>Gross Income (Monthly)</p>

                <input name='' value="$5,000"/>
                </div>

                <div className='section-right'>
                <p>Monthly Debts</p>
                <input name='' value="$0"/>
                </div>
            </div>

            

            
            <div className='section'>
                <div className='section-left'>
                <p>Loan term </p>

                <input name=''/>
                </div>

                <div className='section-right'>
                <p>Monthly Debts</p>
                <input name=''/>
                </div>
            </div>


            <div className='section'>
                <div className='section-left'>
                <p>Home Price</p>

                <input name=''/>
                </div>

                <div className='section-right'>
                <p>Down Payment</p>
                <input name=''/>
                </div>
            </div>


            <div className='section'>
                <div className='section-left'>
                <p>Prop Tax (Yearly) </p>

                <input name=''/>
                </div>

                <div className='section-right'>
                <p>Homeowners Insurance(Yearly)</p>
                <input name=''/>
                </div>
            </div>
        

        </div>



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