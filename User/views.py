from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationForm


class PasswordResetMPSEmailView(PasswordResetView):
    PasswordResetView.extra_email_context = {'mps_site_name': 'My Personal Space'}


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
