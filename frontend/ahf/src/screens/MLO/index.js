import React from 'react';
import "./index.css"
import "./comp_plan.css"
import "./payment.css"
import VideoComponent from '../../components/video';


function DashBoard() {
  return (
    <div>
        <div class="container">
        <div class="header">
            <div class="logo"></div>
            <nav>
                <ul>
                    <li><a href="#">Calculator</a></li>
                    <li><a href="#">Affordability Calculator</a></li>
                    <li><a href="#">Purchase</a></li>
                    <li><a href="#">Refinance</a></li>
                    <li><a href="#">Rent vs Buy</a></li>
                    <li><a href="#">VA Purchase</a></li>
                    <li><a href="#">VA Refinance</a></li>
                    <li><a href="#">Debt-Service(DSCR)</a></li>
                    <li><a href="#">Fix & Flip</a></li>
                </ul>
            
            </nav>
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
        

            <div class="hero-image">
            </div>
        </div>




        <div class="payement">

        </div>
        <div class="loan">
    
          <h5>Loan Detail</h5>
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
        <div class="summery">

        </div>
        
    </div>
    </div>
  );
}

export default DashBoard;