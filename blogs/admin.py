from django.contrib import admin
from blogs.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','headline','created_at', 'published')
    list_filter = ('created_at',)
    search_fields = ('headline',)

