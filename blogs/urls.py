from django.urls import path
from blogs.views import ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleListView, ArticleDeleteView

app_name = 'blogs'

urlpatterns = [
    path('article/new/', ArticleCreateView.as_view(), name='article_form'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]