import React, { useEffect, useLayoutEffect, useState } from 'react';
import VideoComponent from '../video';
import "./index.css"
import axios from 'axios';
import { useSelector } from 'react-redux';


const CompPlan = () => {
    
  const [above_data,setAboveData] = useState([])
  const [flatFee,setFlatFee]  = useState(0)
  const [ff1000,setFF1000]  = useState(0)
  const [percentage,setPercentage] = useState(0)
  const [max,setMax]  = useState(0)
  const [loanBreakPoint,setloanBreakPoint]  = useState(0)
  const [split,setSplit] = useState(0)
  const refreshToken = useSelector((state) => state.auth.refreshToken);

  const headers = {
    Authorization: `JWT ${refreshToken}`,
  };

  function getData() {  
    axios.get(`http://127.0.0.1:8000/api/comp-plan/`,{ headers })
      .then((res) => res.json())
      .then((data) => console.log("data=",data))
      .catch((error) => console.error(error))
  }
  getData()

  return (
    <div className="comp_plan">
      <div className="hero-content">
        <div className="comp_plan_title_container">
          <p className="comp_plan_title">Wholesale comp plan</p>
        </div>

        <div>
          <VideoComponent />
        </div>

        <div className="comp_plan_nav">
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
   
      <div className="section">
        <div className="section-left">
          <p>Flat Fee</p>
          <input
            name=""
            value={flatFee}
            onChange={(e) => setFlatFee(e.target.value)}
          />
        </div>
        <div className="section-right">
          <p className='text-start px-10'>Percentage(0.000% -2.75%)</p>
          <input
            name=""
            value={ff1000}
            onChange={(e) => setFlatFee(e.target.value)}
          />
        </div>
      </div>

      <div className="section">
        <div className="section-left">
          <p className='text-start'>Minimum Compensation ($0 -$2,750)</p>
          <input
            name=""
            value={percentage}
            onChange={(e) => setPercentage(e.target.value)}
          />
        </div>
        <div className="section-right">
          <p className='text-start  px-2'>Maximum Compensation (Min. Comp -$40,000)</p>
          <input
            name=""
            value={max}
            onChange={(e) => setMax(e.target.value)}
          />
        </div>
      </div>

      <div className="section">
        <div className="section-left">
          <p>Max</p>
          <input
            name=""
            value={loanBreakPoint}
            onChange={(e) => setloanBreakPoint(e.target.value)}
          />
        </div>
        <div className="section-right">
          <p> Comp Percentage</p>
          <input
            name=""
            value={split}
            onChange={(e) => setSplit(e.target.value)}
          />
        </div>
      </div>

      <div className="section">
        <div className="section-left">
          <p>Loan break point</p>
          <input
            name=""
            value={loanBreakPoint}
            onChange={(e) => setloanBreakPoint(e.target.value)}
          />
        </div>
        <div className="section-right">
          <p>Split</p>
          <input
            name=""
            value={split}
            onChange={(e) => setSplit(e.target.value)}
          />
        </div>
      </div>
    </div>
  );
};

export default CompPlan;