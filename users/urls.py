from django.urls import path
from .views import RegisterView, CustomLoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]