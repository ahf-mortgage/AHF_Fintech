from django.shortcuts import render
from apps.recruiter.models import *
from apps.RevenueShare.models import *
from .linked_list import LinkedList
import logging
from colorlog import ColoredFormatter
from django.shortcuts import HttpResponse
    
import matplotlib.pyplot as plt
import networkx as nx

from django.http import HttpResponse, HttpResponseServerError
import matplotlib.pyplot as plt
import networkx as nx
import os


def revenue_view(request):
    context = {
        
    }
    return render(request,"home/entry.html",context)



all_revenues  = RevenueShare.objects.all()
total_all_revenue_share = 0
for revenue in all_revenues:
    total_all_revenue_share += revenue.annual_revenue_share.percentage




def visualize_graph(request):
    try:
        # Retrieve all the nodes and edges from the database
        nodes = MLO_AGENT.objects.all()
        edges = Edge.objects.all()
        # Create a directed graph using NetworkX
        G = nx.DiGraph()
        # Add nodes to the graph
        for node in nodes:
            G.add_node(node.user.username, label=node.user.username)
        # Add edges to the graph
        for edge in edges:
            G.add_edge(edge.from_node.user.username, edge.to_node.user.username, weight=edge.weight)
        # Create the graph visualization
        pos = nx.spring_layout(G)
        plt.figure(figsize=(6, 4))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', width=1, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']:.2f}" for u, v, d in G.edges(data=True)})
        plt.title('Graph Visualization')
        # Save the figure to a file
        image_path = os.path.join(os.path.dirname(__file__), 'graph.png')
        plt.savefig(image_path)
        # Return the image as an HttpResponse
        with open(image_path, 'rb') as image_file:
            return HttpResponse(image_file.read(), content_type='image/png')
    except Exception as e:
        # Handle any exceptions that occur during the image generation
        return HttpResponseServerError(f'Error generating the graph image: {str(e)}')

def mlo_linked_list(request):
    
    agents = MLO_AGENT.objects.all()[:5]
  
   
 
    # counter = 0
    # for agent in agents:
    #     ll.sponsor(agent)
    #     if counter == 0:
            
    #         Edge.objects.create(from_node = ahf,to_node = agent,production = 550)
    #     else:
    #         Edge.objects.create(from_node = agents[counter - 1],to_node = agent,production = 550)
    #     counter += 1
    
 
        
    ll     = LinkedList()
    ahf      = MLO_AGENT.objects.get(user__username = "ahf")
    john     = MLO_AGENT.objects.get(user__username = "John")
    sally    = MLO_AGENT.objects.get(user__username = "Sally")
    elif_    = MLO_AGENT.objects.get(user__username = "Elif")
    douglas  = MLO_AGENT.objects.get(user__username = "Douglas")
    ashton   = MLO_AGENT.objects.get(user__username = "Ashton")
    sylvia   = MLO_AGENT.objects.get(user__username = "Sylvia")
    peter    = MLO_AGENT.objects.get(user__username = "Peter")
    bob      = MLO_AGENT.objects.get(user__username = "Bob")
    james    =  MLO_AGENT.objects.get(user__username = "James")
    
    john_node = MLONode.objects.get(mlo = john)
    sally_node = MLONode.objects.get(mlo = sally)
    elif_node = MLONode.objects.get(mlo = elif_)
    douglas_node   = MLONode.objects.get(mlo = douglas)
    
    ll.sponsor(john_node)
    ll.sponsor(sally)
    ll.sponsor(elif_node)
    ll.sponsor(douglas_node)
    
    
    
    
    # ll.sponsor(ahf)
    # try:
    #     edge = Edge.objects.filter(from_node = ahf,to_node = john)
    #     if not edge:
    #         Edge.objects.create(from_node = ahf,to_node = john,production =550)
    # except Edge.DoesNotExist as e:
    #     raise e
        
    # ll.sponsor(john)
  
    # try:
    #     edge = Edge.objects.filter(from_node = john,to_node = sally)
    #     if not edge:
    #         Edge.objects.create(from_node = john,to_node = sally,production =550)
       

    # except Edge.DoesNotExist as e:
    #     raise e
    


    # ll.sponsor(sally)    
    # try:
    #     edge = Edge.objects.filter(from_node = sally,to_node = elif_)
    #     if not edge:
    #         Edge.objects.create(from_node = sally,to_node = elif_,production =550)

    # except Edge.DoesNotExist as e:
    #     raise e
    


    
    # ll.sponsor(elif_)
    # try:
    #     edge = Edge.objects.filter(from_node = elif_,to_node = douglas)
    #     if not edge:
    #         Edge.objects.create(from_node = elif_,to_node = douglas,production =550)
    # except Edge.DoesNotExist as e:
    #     raise e
  
    
    # ll.sponsor(douglas)
    # try:
    #     edge = Edge.objects.filter(from_node = douglas,to_node = ashton)
    #     if not edge:
    #         Edge.objects.create(from_node = douglas,to_node = ashton,production =550)
    # except Edge.DoesNotExist as e:
    #     raise e

    
    
    # ll.sponsor(ashton)
    # try:
    #     edge = Edge.objects.filter(from_node = ashton,to_node = sylvia)
    #     if not edge:
    #         Edge.objects.create(from_node = ashton,to_node = sylvia,production =550)
    # except Edge.DoesNotExist as e:
    #     raise e

    
    
    # ll.sponsor(sylvia)
    # try:
    #     edge = Edge.objects.filter(from_node = sylvia,to_node = peter)
    #     if not edge:
    #         Edge.objects.create(from_node = sylvia,to_node = peter,production =550)
    # except Edge.DoesNotExist as e:
    #     raise e
    

    # ll.sponsor(peter)
    # try:
    #     edge = Edge.objects.filter(from_node = peter,to_node = bob)
    #     if not edge:
    #         Edge.objects.create(from_node = peter,to_node = bob,production =550)
    # except Edge.DoesNotExist as e:
    #     raise e
    
    # ll.sponsor(bob)
    
    current_user     = MLO_AGENT.objects.get(user = request.user)
    current_mlo_node = MLONode.objects.get(mlo = current_user)
    
    
    
    ll.traverse_from_node(current_mlo_node)




    # mlo_agent = MLO_AGENT.objects.all().last() #filter(user = request.user).first()
    # level_balance = {
    #         '1':481,
    #         '2':550,
    #         '3':344,
    #         '4':206,
    #         '5':138,
    #         '6':344 
            
    #     }
    # level = 1
    # while mlo_agent.NMLS_ID_SPONSOR and level < 6 :
    #     mlo_agent = mlo_agent.NMLS_ID_SPONSOR
    #     print(f"sponsor id = {mlo_agent} level={level} commission={level_balance[f'{level}']}")
    #     level += 1
    

    

