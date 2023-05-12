from django.contrib import messages
from django.shortcuts import redirect, render
from blog.models import BlogModel
from django.views.decorators.cache import cache_page
from .forms import CommentForm


@cache_page(600)  # 600sec == 10 min
def home_view(request):
    queryset = BlogModel.objects.order_by('-id')[:3]
    context = {"blog": queryset}

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "نظر شما با موفقیت ثبت شد")
        else:
            messages.warning(request, f"لطفا اطلاعات را به درستی وارد کنید")

        return redirect("home:home")

    return render(request, "home/home.html", context)
