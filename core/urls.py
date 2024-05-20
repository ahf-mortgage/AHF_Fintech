
from django.contrib import admin
from django.urls import path,include
from utils.views import AhfSignupView

urlpatterns = [
    path('',include("apps.home.urls",namespace = "home")),
    path('user/W2branchYearlyGross/',include('apps.W2branchYearlyGross.urls',namespace="W2branchYearlyGross")),
    path('admin/', admin.site.urls),
]
