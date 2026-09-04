from django.urls import path
from .views import ProductListView, ContactView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/',ProductDetailView.as_view(), name='product_detail'),

]