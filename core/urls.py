
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from .views import  visualize_graph,mlo_detail,loan_detail,error_view
from django.conf import settings
from django.conf.urls.static import static


def react_view(request):
    return render(request,"build/index.html")

urlpatterns = [
    path('',include("apps.home.urls",namespace = "home")),
    path('error/',error_view,name="error"),
    path("account/", include("apps.accounts.urls")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('graph/',include("apps.recruiter.urls")),
    path('user/W2branchYearlyGross/',include('apps.W2branchYearlyGross.urls',namespace="W2branchYearlyGross")),
    path('revenue/',include('apps.recruiter.urls',namespace="revenue")),
    path('admin/', admin.site.urls),
    path("front/",react_view,name = "react_view"),
    path("visualize/",visualize_graph,name = "visualize_graph"),
    path("loan-detail/",loan_detail,name = "loan-detail"),
    path("mlo_detail/<name>/",mlo_detail,name = "mlo_detail")

    ]
if True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)