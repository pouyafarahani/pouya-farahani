from django.views.generic import DetailView, ListView

from home.views import BlogModel


class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = BlogModel
    context_object_name = 'blog'
    paginate_by = 6


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = BlogModel
    context_object_name = 'blog'
