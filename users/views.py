from django.views.generic import CreateView
from users.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:home')




