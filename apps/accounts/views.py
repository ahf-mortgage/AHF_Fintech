import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegistrationForm
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from jsonview.decorators import json_view
from .models import OTP




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("user name ",user)
        if user is not None:
            login(request, user)
            return redirect('/get-sponsor/')  # Replace 'home' with the name of your home URL
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login') 



def verfiy_otp(request,user_id):
    user = User.objects.filter(id = user_id).first()
    context = {
        "user":user
    }
    if request.method == "POST":
        # request.POST.pop("csrfmiddlewaretoken")
        values = list(request.POST.values())[1:]
        values = "".join(values)
        user_otp = values
        system_otp = OTP.objects.filter(user = user).last()
        time_delta = timezone.now() - system_otp.generated_at
        print("time delta = ",time_delta.min)
        system_otp = system_otp.otp_code
        if user_otp == str(system_otp):
            user.is_active = True
            user.save()
            return redirect("login")
        else:
            messages.add_message(request, messages.INFO, "Invalid or expired OTP.")
            return render(request, 'otp_verfiy.html',context=context)
            print("system otp =",system_otp)
            print("user otp ",user_otp)

    return render(request, 'otp_verfiy.html',context=context)




def send_otp_email(user_email, otp_code):
    subject = 'Your OTP Code'
    message = f'Your One-Time Password (OTP) is: {otp_code}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        print("OTP email sent successfully.")
    except Exception as e:
        print(f"Failed to send OTP email: {e}")






def generate_six_digit_otp():
    # Generate a random number between 100000 and 999999
    otp = random.randint(1000, 9999)
    return otp





def sign_up(request):
    user_form = UserRegistrationForm()
    gerrors = []
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST or None)
        if user_form.is_valid():
       
            user = user_form.save(commit=False)
            user.save()
            otp = generate_six_digit_otp()
            user = user_form.save(commit=False)
            OTP.objects.create(user=user, otp_code=otp)
            send_otp_email(user.email,otp)
            return  redirect(f"/account/verfiy/{user.id}")

        else:
            for error in user_form.errors.as_data():
                _error =  user_form.errors.as_data().get(error,None)
                for e in _error:
                    for f in e:
                       print("errors = ",f)
                       gerrors.append(f)

            return render(request, 'signup.html',{"errors":gerrors,"form":user_form})
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