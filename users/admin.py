from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': ('phone_number', 'country', 'avatar'),
        }),
    )

    list_display = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'country', 'is_staff', 'is_active')


admin.site.register(CustomUser, CustomUserAdmin)