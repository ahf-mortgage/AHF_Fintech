
from django.contrib import admin
from django.urls import path,include
# from utils.views import AhfSignupView

urlpatterns = [
    path('',include("apps.home.urls",namespace = "home")),
    path("account/", include("account.urls")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('graph/',include("apps.recruiter.urls")),
    path('user/W2branchYearlyGross/',include('apps.W2branchYearlyGross.urls',namespace="W2branchYearlyGross")),
    path('revenue/',include('apps.recruiter.urls',namespace="revenue")),
    path('admin/', admin.site.urls),
]
