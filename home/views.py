from django.shortcuts import redirect
from django.views.generic import ListView
from django.views import View
from django.contrib import messages

from blog.models import BlogModel
from .forms import CommentForm


class HomeView(ListView, View):
    model = BlogModel
    template_name = 'home/home.html'
    context_object_name = 'blog'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-id')[:3]

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد')
            return redirect('home:home')
        messages.warning(request, f'لطفا اطلاعات را به درستی وارد کنید')
        return redirect('home:home')
