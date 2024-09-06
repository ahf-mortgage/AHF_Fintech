import axios from 'axios';
import React, { useState, useEffect, useRef } from 'react';
import { GraphCanvas,CustomLayoutInputs ,NodePositionArgs} from 'reagraph';
import Dot from '../../components/activity';
import { setShowModal } from '../../context/action';
import "./index.css"
import { useNavigate } from 'react-router-dom';

import {
  useGLTF,
  useCursor,
  useTexture,
  Text,
  Decal,
  Environment,
  OrbitControls,
  RenderTexture,
  RandomizedLight,
  PerspectiveCamera,
  AccumulativeShadows,
  Html
} from '@react-three/drei'
import Box from '../../components/Fiber';

const SimpleDirectedGraph = () => {
  const [fetchedNodes, setFetchedNodes] = useState([])
  const [fetchedEdges, setFetchedEdges] = useState([])
  const [mloInfo, showMLoInfo] = useState(false)
  const [node_id, setNodeId] = useState(0)
  const [parent_id, setParentId] = useState(0)

  const navigate = useNavigate();

  useEffect(() => {
    async function getData() {
      try {
        const data = await axios.get("http://127.0.0.1:8000/api/nodes_views/")
        const nodes = data.data['nodes']
        const edges = data.data['edges']
        setFetchedNodes(nodes)
        setFetchedEdges(edges)

      } catch (error) {

      }
    }

    getData()
  }, [])

  const filteredNodes = fetchedNodes.filter((node) => {
    return fetchedEdges.some(
      (edge) => edge.source === node.id || edge.target === node.id
    );
  });


const handleOnNodeClick = (id) => {
  showMLoInfo(true)
}

const handleCanvasClick = (id) => {
  console.log("node is clicked ",id)
}

  return (
    <div>
      {
    
      fetchedEdges.length > 0 ?

            <div>
             
              {

                <div style={{ width: '100%', height: '100%' }}>


                  <GraphCanvas
                    layoutType='hierarchicalTd'
                    sizingType='centrality'
                    minNodeSize={10}
                    minDistance={200}

                    
                    draggable={true}
                    onNodeClick={
                      (node) => {
                        setNodeId(node.id)
                        navigate(`/detail/?id=${node.id}`)
                        if (node.id == 30011) {
                          setParentId(0)
                        }
                        else {
                          setParentId(node.parents[0].id)
                        }

                      }
                    }
                    
                    onNodeDoubleClick={(node) => console.log("hello world=",node.id)}
                    onEdgeClick={(edge) => {
                      const edge_id = edge.id
                        axios.get(`http://127.0.0.1:8000/api/get-all-nodes/?q=${edge_id}`)
                             
                             .then((data) => {
                               navigate("/graph")
                             })
                             .catch((error) => console.log("error=",error))
                    }} 
                    // layoutOverrides={{
                    //   getNodePosition: (id, { nodes }) => {
                    //     const idx = nodes.findIndex(n => n.id === id);
                    //     const node = nodes[idx];
                    //       // Define custom positions
                    //       const x = 100 * (idx % 2);  // Toggle x position based on index (0 or 100)
                    //       const y = 100 * Math.floor(idx / 2);  // Increment y for every two nodes
                    //       const z = 1;  // Fixed z-index
                    //       return { x, y, z };
                                            
                    //   }
                    // }}                   
                    nodes={filteredNodes}
                    edges={fetchedEdges}

                    renderNode={({ size, color, opacity }) => (
                      <group>
                        <mesh>
                          <boxGeometry attach="geometry" args={[size * 3, size * 3, 1]} /> {/* Rectangle dimensions */}
                          <meshBasicMaterial
                            attach="material"
                            color={color}
                            opacity={opacity}
                            transparent
                          />
                        </mesh>
                      </group>
                    )}
                  
                  >
                  
                </GraphCanvas>
                </div>

              }
             
            </div>
            
            :
            <div className='h-screen w-screen flex flex-col justify-center text-center'>
              <Dot size={40} />

            </div>
      }
    </div>


  );
};




export default SimpleDirectedGraph;

