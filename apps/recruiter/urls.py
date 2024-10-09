
from django.contrib import admin
from django.urls import path,include
from . import plot,api
from .views import register_new_mlo,single_loan_detail,delete_node

app_name = "revenue"
urlpatterns = [
    path('',plot.graph_view,name="graph"),
    path('api/',api.RecruiterAPIView.as_view(),name='api-view'),
    path('mlo_views/',api.NodeGraphView.as_view(),name = "mlo-views"),
    path('register/<node_id>/',register_new_mlo,name="register-new-mlo"),
    path('delete/<node_id>/',delete_node,name="delete-node"),
    path("single-loan-detail/",single_loan_detail,name="single-loan-detail")
    
   
   
]
