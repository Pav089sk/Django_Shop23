from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Contact, ContactsShop

# Create your views here.
def home(request):
    last_five_products = Product.objects.order_by('-created_at')[:5]
    for product in last_five_products:
        print(f"Продукт: {product.name}, цена: {product.price}")

    return render(request, "catalog/home.html")

def contacts(request):
    contacts_list = Contact.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name)
        print(phone)
        print(message)
        return HttpResponse(f"Благодарим Вас, {name}! Ваш телефон - {phone}\n"
                            f"Ваше сообщение получено.")
    return render(request, "catalog/contacts.html", {"contacts": contacts_list})

