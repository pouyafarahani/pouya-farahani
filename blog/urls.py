from django.urls import path

from .views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('list', BlogListView.as_view(), name='blog_list'),
    path('list', BlogDetailView.as_view(), name='blog_detail'),
]
