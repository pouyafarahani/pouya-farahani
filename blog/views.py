from django.shortcuts import render
from django.views import View


class BlogListView(View):
    def get(self, request):
        return render(request, 'blog/blog_list.html')


class BlogDetailView(View):
    def get(self, request):
        return render(request, 'blog/blog_detail.html')
