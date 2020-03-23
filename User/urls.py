from django.urls import path
from .views import PasswordResetMPSEmailView, SignUpView, edit_profile
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView,\
    PasswordResetDoneView, PasswordResetConfirmView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path('change-password/', PasswordChangeView.as_view(), name='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset-form/', PasswordResetMPSEmailView.as_view(), name='password_reset_form'),
    path('password-reset-done-form/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('review/', TemplateView.as_view(template_name='review.html'), name='review'),
    path('classes/', login_required(TemplateView.as_view( template_name='classes.html')), name='classes'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    #path('profile/', ProfileChangeView.as_view(template_name='profile.html'), name='profile'),
    path('profile/', views.edit_profile, name='profile')
]

