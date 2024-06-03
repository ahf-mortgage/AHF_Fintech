
from apps.recruiter.models import MLO_AGENT_PRODUCTION, MLONode,MLO_AGENT
from apps.recruiter.graphs import dfs
from apps.recruiter.graphs import bfs


class Node:
    def __init__(self,mlo_agent):
        self.mlo_agent = mlo_agent
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sponsor(self, graph):
        new_node = Node(graph)
        
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node



    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.mlo_agent)
            current_node = current_node.next
            
    def traverse_from_node(self, start_mlo_agent):

    
    
            
        # Set up the logger
        mlo_prod = start_mlo_agent.mlo
        mlo_agent_production = MLO_AGENT_PRODUCTION.objects.get(NMLS_ID =mlo_prod)
        total_production = 0
        level = 1
        level_to_amount = { 
                          
                        "1":481,
                        "2":550, 
                        "3":344, 
                        "4":206, 
                        "5":138, 
                        "6":344, 
                        "7":688,
                        "8":0
                        }
        
        
      
        current_node = self.head
        while current_node.next:
            if current_node.mlo_agent == start_mlo_agent:
                break
            current_node = current_node.next

        if current_node.next:
            while current_node.next:
                total_production += level_to_amount.get(f"{level}",0)
                print(f"{start_mlo_agent} on level= {level} gets  {level_to_amount.get(f'{level}')}  from mlo {current_node.next.mlo_agent}")
                current_mlo = MLO_AGENT.objects.filter(user__username = current_node.mlo_agent).first()
                current_mlo_node = MLONode.objects.filter(mlo = current_mlo).first()
           
                  
                if current_mlo_node:
                    print(list(bfs(current_mlo_node)))
                    num_of_mlo = len(list(bfs(current_mlo_node)))
                    if level == 1 and  num_of_mlo < 2:
                        break
                    if level == 2 and num_of_mlo < 6:
                        break
                    
                    if level == 3 and  num_of_mlo < 11:
                        break
                    if level == 4 and num_of_mlo < 16:
                        break
                    
                    if level == 5 and  num_of_mlo < 21:
                        break
                    if level == 6 and num_of_mlo < 26:
                        break
                    
                    if level == 7 and num_of_mlo < 41:
                        break
                    
              

                current_node = current_node.next
                level += 1
            mlo_agent_production.total = max(mlo_agent_production.total,total_production)
            mlo_agent_production.save()
        else:
            print(f"Node with mlo_agent '{start_mlo_agent}' not found in the list.")
            
        
