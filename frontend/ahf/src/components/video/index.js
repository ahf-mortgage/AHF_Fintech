import ReactPlayer from 'react-player'
import React from 'react';
import "./index.css"


const VideoComponent = () => {
  return (
    <div className='vid_container'>
        <ReactPlayer 
        url='https://youtu.be/fbezt0B1-vA'
        width="281px"
        height="143.39px"

        style={
            {

                width: "281px",
                height: "143.39px",
                top: "202px",
                left: "90px",
                gap: "0px",
                opacity: "0px"
            
            }
        }/>
    </div>
  );
};

export default VideoComponent;