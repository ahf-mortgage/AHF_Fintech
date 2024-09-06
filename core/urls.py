
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from .views import graph_view
# from utils.views import AhfSignupView

def react_view(request):
    return render(request,"build/index.html")

urlpatterns = [
    path('',include("apps.home.urls",namespace = "home")),
    path("account/", include("apps.accounts.urls")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('graph/',include("apps.recruiter.urls")),
    path('user/W2branchYearlyGross/',include('apps.W2branchYearlyGross.urls',namespace="W2branchYearlyGross")),
    path('revenue/',include('apps.recruiter.urls',namespace="revenue")),
    path('admin/', admin.site.urls),
    path("front/",react_view,name = "react_view"),
    path("graph/",graph_view,name="graph-view")
]
