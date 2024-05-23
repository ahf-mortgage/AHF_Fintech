from django.shortcuts import render
from .models import *

def revenue_view(request):
    context = {
        
    }
    return render(request,"home/entry.html",context)
