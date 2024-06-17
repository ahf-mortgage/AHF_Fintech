import React from 'react';
import "./index.css"

const HorizontalLine = ({width,color}) => {
  return (
    <hr className='horizontal-line' style={{width:width,backgroundColor:color}} />
  );
};

export default HorizontalLine;