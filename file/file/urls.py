from django.contrib import admin
from django.urls import path
from .views import FileViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',FileViewSet.as_view(),name="FileViewSet")
]
