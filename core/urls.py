
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include("home.urls")),
    path('admin/', admin.site.urls),
    path('accounts/two-factor/', include('allauth_2fa.urls')),
    path('accounts/', include('allauth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
