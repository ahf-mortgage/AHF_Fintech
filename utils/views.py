from allauth.account.views import SignupView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import AHFSignupForm

class AhfSignupView(SignupView):
    form_class = AHFSignupForm
    template_name = 'account/signup.html'  
    success_url = reverse_lazy('/') 
    
    @classmethod
    def as_view(cls, **kwargs):
            view = super().as_view(**kwargs)
            return view
    
    