from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegistrationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("user name ",user)
        if user is not None:
            login(request, user)
            return redirect('/')  # Replace 'home' with the name of your home URL
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    


def sign_up(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST or None)
        # print("before validation  = ",user_form)
        if user_form.is_valid():
            print("form is valid = ",user_form.cleaned_data)
            user_form.save()
            return redirect(reverse("login"))
        else:
            print("errors=",)
            for error in user_form.errors.get_json_data():
                print("errors - ",error)
            return render(request, 'signup.html',{"errors":user_form.errors})
    else:
        return render(request, 'signup.html')