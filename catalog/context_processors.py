from .models import ContactsShop

def contacts_shop(request):
    contact = ContactsShop.objects.last()
    return {'contacts_shop': contact}