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
from .draw import draw

@login_required
def graph_view(request):
    start_node,visited, node_list,total_mlo_sponsored = dfs_traversal(request)
    node_graphs = []
    # list(node_list.keys())[0]
    for child in node_list.keys():
        graph_image = draw(request,child)
        node_graphs.append(child)
    # print("node_graphs=",node_graphs)
    return render(request, 'graph.html', {'graph_image': graph_image})



