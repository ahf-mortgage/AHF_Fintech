import logging
from colorlog import ColoredFormatter
from apps.recruiter.models import MLO_AGENT_PRODUCTION
class Node:
    def __init__(self,mlo_agent):
        self.mlo_agent = mlo_agent
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sponsor(self, data):
        new_node = Node(data)
        
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
        mlo_agent_production = MLO_AGENT_PRODUCTION.objects.get(NMLS_ID =start_mlo_agent)
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
                current_node = current_node.next
                level += 1
            mlo_agent_production.total = max(mlo_agent_production.total,total_production)
            mlo_agent_production.save()
        else:
            print(f"Node with mlo_agent '{start_mlo_agent}' not found in the list.")
            
        
