import axios from 'axios';
import { Label } from 'flowbite-react';
import React, { useState, useEffect } from 'react';
import { GraphCanvas } from 'reagraph';
import Dot from '../../components/activity';
import { ModalBox } from '../../components/modal';
import { useDispatch, useSelector } from 'react-redux';
import { setShowModal } from '../../context/action';






const SimpleDirectedGraph = () => {
  const [fetchedNodes, setFetchedNodes] = useState([])
  const [fetchedEdges, setFetchedEdges] = useState([])
  const [bfsNodes, setBFSNodes]         = useState([]);
  const [node_id, setNodeId]            = useState(0)
  const [parent_id, setParentId]        = useState(0)
  const dispatch                        = useDispatch();
  const showModal                       = useSelector((state) => state._showModalReducer)

  console.log("showModal=",showModal)

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




  return (
    <div>
      {
        fetchedEdges.length > 0 ?
          <div>
            {
              showModal ?
                <ModalBox id={node_id} parent_id={parent_id} />
                :
                <div>

                  <GraphCanvas
                    layoutType='hierarchicalTd'
                    edgeArrowPosition='end'
                    sizingType='none'
                    minNodeSize={20}
                    minDistance={60}
                    onNodePointerOver={
                      (node) => {
                        setNodeId(node.id)
                        setParentId(node.parents[0].id)
                        dispatch(setShowModal(true));
                      }
                    }
                  
                    nodes={filteredNodes}
                    edges={fetchedEdges}

                  />


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
