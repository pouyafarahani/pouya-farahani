from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView
from home.views import BlogModel


@method_decorator(cache_page(600), name='dispatch')  # 600sec == 10 min
class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = BlogModel
    context_object_name = 'blog'
    paginate_by = 6


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = BlogModel
    context_object_name = 'blog'
