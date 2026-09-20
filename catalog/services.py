from catalog.models import Product

def product_of_category(category_id):
    return Product.objects.filter(category=category_id, publication_status=True)
