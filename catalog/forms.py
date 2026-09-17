from django import forms
from .models import Contact, Product
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
                     'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Цена товара',
            'min': '0',
            'step': '0.01'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-select'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })


    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name:
            return name
        low_name = name.lower()
        for word in self.FORBIDDEN_WORDS:
            if word in low_name:
                raise ValidationError (f'Наименование продукта содержит запрещенное слово {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            return description
        low_desc = description.lower()
        for word in self.FORBIDDEN_WORDS:
            if word in low_desc:
                raise ValidationError (f'В описании продукта содержится запрещенное слово {word}')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError (f'Вы ввели {price}. Цена не может быть отрицательной')
        return price