from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "catalog/home.html")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name)
        print(phone)
        print(message)
        return HttpResponse(f"Благодарим Вас, {name}! Ваш телефон - {phone}\n"
                            f"Ваше сообщение получено.")
    return render(request, "catalog/contacts.html")