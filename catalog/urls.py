from django.urls import path
from .views import ProductListView, ContactView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = 'catalog'

urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
    path('product/new/',ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/',ProductUpdateView.as_view(), name='product_update'),

]