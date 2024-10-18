import random
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.recruiter.models import Edge,MLO_AGENT
from apps.recruiter.forms import EdgeForm
from django.contrib.auth.models import User
import matplotlib.pyplot as plt
import os



@login_required
def mlo_detail(request,name):
    print("name = ",name)
    render(request, 'screens/graph/index.html', {"data":[]})



@login_required
def visualize_graph(request):
    edges = Edge.objects.all()
    data = []
    children = []
    if request.method == "POST":
        mlo_name = request.POST.get("mlo_name",None)
        mlo = MLO_AGENT.objects.filter(user__username = mlo_name).first()
        mlo.delete()
        
    
    for edge in edges:
        print(edge.source_node.mlo_agent.user.username,request.user.username)
        data.append({f"{edge.source_node.mlo_agent.user.username}":edge.target_node.mlo_agent.user.username})
     
    
    grouped = {}

    for entry in data:
        for key, value in entry.items():
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(value)

    names = data
    children = children
    return render(request, 'screens/graph/index.html', {"data":grouped})



@login_required
def loan_detail(request,id,level):
    print("id ========  ",id)
    try:
        user = User.objects.filter(id = id).first()
    except User.DoesNotExist as e:
        raise e
    request.mlo_user = user
    
    context = {
        "id":id,
        "user":user,
        "level":level
    }
    return render(request, 'screens/table/loan_detail.html',context)



@login_required
def get_sponsor(request):    

    context = {

        "form":EdgeForm()
    
    }
    return render(request, 'screens/agents/agent_onboarding.html',context)



def error_view(request):
    return render(request, 'screens/404.html')


