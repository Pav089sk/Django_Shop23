from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.TextField(max_length=100, verbose_name='Наименование категории')
    description = models.TextField(max_length=250, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description= models.CharField(max_length=250, verbose_name='Описание')
    image = models.ImageField(upload_to='images/',null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category,
        on_delete=models.PROTECT,
        verbose_name='Категория')

    price = models.DecimalField(max_digits=10, decimal_places=2,
                              default='0.00', verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    publication_status = models.BooleanField(default=False, verbose_name = 'Статус публикации')
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='products', null=False, blank=False)

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']
        permissions = [('can_unpublish_product', 'Can unpublish product'),
                       ]

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.name

class ContactsShop(models.Model):
    country = models.CharField('Страна', max_length=100, default='Россия')
    inn = models.CharField('ИНН', max_length=20, default='77-1234321')
    address = models.CharField('Адрес', max_length=200, default='Москва, Якиманка, Ленинский проспект 1А')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Контакт магазина'
        verbose_name_plural = 'Контакты магазина'

