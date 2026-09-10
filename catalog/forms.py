from django import forms
from .models import Contact, Product
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']



class ProductForm(forms.ModelForm):
    DANGERS_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
                     'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name:
            return name
        low_name = name.lower()
        for word in self.DANGERS_WORDS:
            if word in low_name:
                raise ValidationError (f'Наименование продукта содержит запрещенное слово {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            return description
        low_desc = description.lower()
        for word in self.DANGERS_WORDS:
            if word in low_desc:
                raise ValidationError (f'В описании продукта содержится запрещенное слово {word}')
        return description
