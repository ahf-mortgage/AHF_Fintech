from django.shortcuts import render
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
from .views import bfs_traversal,dfs_traversal
from .models import MLO_AGENT,Node
from django.contrib.auth.decorators import login_required
import random
from matplotlib.colors import to_hex
import cv2
import numpy as np


@login_required
def graph_view(request):
    # Call the bfs_traversal function to get the visited nodes and node_list
    start_node,visited, node_list,total_mlo_sponsored = dfs_traversal(request)

    # Create the directed graph
    G = nx.DiGraph()
    level_for_amount = {
        "1":481.25,
        "2":550.0,
        "3":343.75,
        "4":137.5,
        "5":343.75,
        "6":687.5
        
        
    }

    # Add nodes
    for user in node_list:
        G.add_node(f"{user.username}")

    # Add edges
    edge_labels = {}
    level = 1
    total = 0
    edge_colors = []
    for parent, children in node_list.items():
        parent_username = parent.username
        for child in children:
            total += level_for_amount[f'{level}']
            edge_label = f"{request.user.username} get {level_for_amount[f'{level}']} from {child['node']}"
            G.add_edge(parent_username, f"{child['node'].username}")
            edge_labels[(parent.username, f"{child['node'].username}")] = edge_label
            # Generate a random color
            r = random.uniform(0, 1)
            g = random.uniform(0, 1)
            b = random.uniform(0, 1)
            edge_color = to_hex((r, g, b))
            G.add_edge(parent.username, f"{child['node'].username}")
            edge_labels[(parent.username, f"{child['node'].username}")] = edge_label
            edge_colors.append(edge_color)
        print(f"{request.user.username} gets {total} in level {level} from {children}")
        level += 1

    # Create the graph image
    fig = plt.figure(figsize=(8, 6))
    start_node = start_node.username
    
    pos = nx.bfs_layout(G,start_node,align="horizontal")

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size = 1000 * 3,edge_color='gray', font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    # Create the legend
    labels_data = [
        f"gets ${total}",
        f"sponsored {total_mlo_sponsored} mlos"
    ]
    unique_edge_colors = set(edge_colors)
    legend_elements = [
        plt.Line2D([0], [0], color=list(unique_edge_colors)[random.randint(1,3)], lw=2, label=f'{request.user.username} {data} ')
        for data in labels_data
    ]
    
    # legend_elements = [plt.Line2D([0], [0], color= list(unique_edge_colors)[0], lw=2, label=f'{request.user.username} gets  ${total}')]
    plt.legend(handles=legend_elements, loc='lower left', fontsize=10)

    # Convert the graph image to a base64-encoded string
    buf = io.BytesIO()
    plt.savefig(buf, format='png')

    img = cv2.imdecode(np.frombuffer(buf.getvalue(), np.uint8), cv2.IMREAD_COLOR)
    img_inverted = cv2.bitwise_not(img)
    graph_image_flipped = cv2.flip(img, 0)

     # Convert the inverted image back to a buffer
    _, buffer   = cv2.imencode('.png', img_inverted)
    graph_image = base64.b64encode(buffer).decode('utf-8')

    return render(request, 'graph.html', {'graph_image': graph_image})



