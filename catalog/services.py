from catalog.models import Product
from django.core.cache import cache

def product_of_category(category_id):
    cache_key = f'category_{category_id}'
    queryset = cache.get(cache_key)
    if not queryset:
        queryset = Product.objects.filter(category=category_id, publication_status=True)
        cache.set(cache_key, queryset, 60 * 5)
    return queryset

