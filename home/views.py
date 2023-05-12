from django.shortcuts import render
from django.views.decorators.cache import cache_page

from blog.models import BlogModel


@cache_page(600)  # 600sec == 10 min
def home_view(request):
    queryset = BlogModel.objects.order_by('-id')[:3]
    context = {"blog": queryset}
    return render(request, "home/home.html", context)
