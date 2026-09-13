from django.views.generic import CreateView
from users.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.conf import settings

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        print(f"=== ОТПРАВКА ПИСЬМА на {user_email} ===")
        print(f"From: {settings.DEFAULT_FROM_EMAIL}")
        send_mail(
            subject='Добро пожаловать!',
            message='Спасибо за регистрацию!',
            recipient_list=[user_email],
            from_email=settings.DEFAULT_FROM_EMAIL,
            fail_silently=False,
        )

    print("=== ПИСЬМО ОТПРАВЛЕНО БЕЗ ОШИБОК ===")

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:home')




