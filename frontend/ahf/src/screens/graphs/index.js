import axios from 'axios';
import React, { useState, useEffect } from 'react';
import { GraphCanvas } from 'reagraph';



const SimpleDirectedGraph = () => {
  const [fetchedNodes,setFetchedNodes] = useState([])
  const [fetchedEdges,setFetchedEdges] = useState([])

  useEffect(() => {
    async function getData() {
      try {
        const data =  await axios.get("http://127.0.0.1:8000/api/nodes_views/")
        const nodes = data.data['nodes']
        const edges = data.data['edges']
        setFetchedNodes(nodes)
        setFetchedEdges(edges)
        
      } catch (error) {
        
      }
    }

    getData()
  },[])




  const filteredNodes = fetchedNodes.filter((node) => {
    return fetchedEdges.some(
      (edge) => edge.source === node.id || edge.target === node.id
    );
  });
console.log("fetchedEdges = ",fetchedEdges)

  return (
    <GraphCanvas
    layoutType='treeTd2d'
    edgeArrowPosition='end'
    sizingType='none'
    minNodeSize={10}
    minDistance={60}

    onNodeClick={(node) => {
      console.log("node=",node)
    }}
    nodes={filteredNodes}
    edges={fetchedEdges}
   
  />
  );
};


export default SimpleDirectedGraph;
