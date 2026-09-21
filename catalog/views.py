from catalog.models import Product, Contact
from catalog.forms import ContactForm, ProductForm
from django.views.generic import  ListView, FormView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from catalog.services import product_of_category


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        is_owner = product.owner == request.user
        is_moderator = request.user.has_perm('catalog.change_product')

        if not (is_owner or is_moderator):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(publication_status=True).order_by('-created_at')[:10]


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:contacts')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context

@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        is_owner = product.owner == request.user
        is_moderator = request.user.has_perm('catalog.delete_product')

        if not (is_owner or is_moderator):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class UpdatePublicationStatus(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У Вас нет права отменить публикацию продукта')

        product.publication_status = False
        product.save()
        return redirect('catalog:home')


class ProductByCategory(ListView):
    model = Product
    template_name = 'catalog/list_products_category.html'
    context_object_name = 'products_by_cat'
    paginate_by = 10
    def get_queryset(self):
        return product_of_category(category_id=self.kwargs['category_id'])