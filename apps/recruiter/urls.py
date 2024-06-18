
from django.contrib import admin
from django.urls import path,include
from . import plot,api

app_name = "revenue"
urlpatterns = [
    path('',plot.graph_view,name="graph"),
    path('api/',api.RecruiterAPIView.as_view(),name='api-view')
   
]
