from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegistrationForm
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from jsonview.decorators import json_view

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
    

def logout_view(request):
    logout(request)
    return redirect('login') 
   


def sign_up(request):
    user_form = UserRegistrationForm()
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
            return render(request, 'signup.html',{"errors":user_form.errors,"form":user_form})
    else:
        return render(request, 'signup.html',{"form":user_form})
    



@json_view
def save_user_form(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        print("form data = ",form.cleaned_data)
      
        form.save()
        return {'success': True}


    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)
    return {'success': False, 'form_html': form_html}