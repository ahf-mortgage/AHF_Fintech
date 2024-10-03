from django.contrib import admin
from django.urls import path,include
from .views import login_view,sign_up,logout_view,save_user_form,verfiy_otp

urlpatterns = [
    path('login/',login_view,name = "login"),
    path('sign-up/',sign_up,name = "sign-up"),
    path('verfiy/<int:user_id>/',verfiy_otp,name = "verfiy-otp"),
    path("validate-form/",save_user_form,name="validate-form"),
    path('logout_view/',logout_view,name = "log-out")

]
