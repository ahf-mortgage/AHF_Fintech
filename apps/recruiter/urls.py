
from django.contrib import admin
from django.urls import path,include
from . import plot,api
from .views import register_new_mlo

app_name = "revenue"
urlpatterns = [
    path('',plot.graph_view,name="graph"),
    path('api/',api.RecruiterAPIView.as_view(),name='api-view'),
    path('mlo_views/',api.NodeGraphView.as_view(),name = "mlo-views"),
    path('register/',register_new_mlo,name="register-new-mlo")
    
   
   
]
