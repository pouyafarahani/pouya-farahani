from django.shortcuts import render
from django.views.generic import ListView

from .models import BlogModel


class HomeView(ListView):
    model = BlogModel
    template_name = 'home/home.html'
    context_object_name = 'blog'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-id')[:3]
