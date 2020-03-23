from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationForm, UserChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse

class PasswordResetMPSEmailView(PasswordResetView):
    PasswordResetView.extra_email_context = {'mps_site_name': 'My Personal Space'}

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = UserChangeForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})