from django.shortcuts import render
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
from .views import bfs_traversal

def graph_view(request):
    # Call the bfs_traversal function to get the visited nodes and node_list
    visited, node_list = bfs_traversal(request)

    # Create the directed graph
    G = nx.DiGraph()

    # Add nodes
    for user in node_list:
        G.add_node(user.username)

    # Add edges
    for parent, children in node_list.items():
        for child in children:
            G.add_edge(parent.username, child["node"].username)

    # Create the graph image
    fig = plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_size=10)

    # Convert the graph image to a base64-encoded string
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    graph_image = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Render the template with the graph image
    return render(request, 'graph.html', {'graph_image': graph_image})