from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from blogs.models import Article

class ArticleCreateView(CreateView):
    model = Article
    fields = ['headline', 'content', 'preview', 'published']
    template_name = 'blogs/article_form.html'
    success_url = reverse_lazy('blogs:article-list')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blogs/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_article += 1
        obj.save()
        return obj

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['headline', 'content', 'preview', 'published']
    template_name = 'blogs/article_upd.html'
    success_url = reverse_lazy('blogs:article-list')

    def get_success_url(self):
        return reverse_lazy('blogs:article_detail', kwargs={'pk': self.object.pk})

class ArticleListView(ListView):
    model = Article
    template_name = 'blogs/articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(published=True)

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blogs/article_confirm_delete.html'
    success_url = reverse_lazy('blogs:article-list')

