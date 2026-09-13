from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import CustomUser
from django import forms

# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email.split('@')[0]
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


# Форма авторизации
class CustomAuthenticationForm(AuthenticationForm):
    pass