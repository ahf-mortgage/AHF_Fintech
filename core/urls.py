
from django.contrib import admin
from django.urls import path,include
from utils.views import AhfSignupView

urlpatterns = [
    path('',include("home.urls")),
    path('user/W2branchYearlyGross/',include('W2branchYearlyGross.urls',namespace="W2branchYearlyGross")),
    path('admin/', admin.site.urls),
    path('accounts/two-factor/', include('allauth_2fa.urls')),
    path('accounts/', include('allauth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
