from django.shortcuts import render
from django.views.generic import DetailView
from django.views import View

from home.views import BlogModel


class BlogListView(View):
    def get(self, request):
        return render(request, 'blog/blog_list.html')


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = BlogModel
    context_object_name = 'blog'
