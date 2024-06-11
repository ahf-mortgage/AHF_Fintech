
from django.contrib import admin
from django.urls import path,include
from . import plot

urlpatterns = [
    path('',plot.graph_view,name="graph"),
   
]
