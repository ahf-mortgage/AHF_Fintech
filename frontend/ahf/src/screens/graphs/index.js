import React from 'react';
import Graph from 'react-graph-vis';

const GraphComponent = () => {
  const graph = {
    nodes: [
      { id: 1, label: 'Node 1' },
      { id: 2, label: 'Node 2' },
      { id: 3, label: 'Node 3' },
      { id: 4, label: 'Node 4' },
      { id: 5, label: 'Node 5' },
      { id: 6, label: 'Node 6' },
    ],
    edges: [
      { from: 1, to: 2 },
      { from: 1, to: 3 },
      { from: 2, to: 4 },
      { from: 2, to: 5 },
      { from: 3, to: 6 },
    ],
  };

  const options = {
    layout: {
      hierarchical: {
        direction: 'TB', // Top-Bottom (root at top)
        sortMethod: 'directed', // Sort based on edge direction
        // Adjust levelSeparation to control spacing between levels
        levelSeparation: 150, // Increase for more space
      },
    },
    physics: {
      enabled: false, // Disable physics simulation (animation)
    },
    edges: {
      color: '#000000',
    },
  };

  const events = {
    select: function (event) {
      var { nodes, edges } = event;
      console.log('Selected nodes:');
      console.log(nodes);
      console.log('Selected edges:');
      console.log(edges);
    },
  };

  return (
    <div>
      <Graph graph={graph} options={options} events={events} style={{ height: '800px' }} />
    </div>
  );
};

export default GraphComponent;
