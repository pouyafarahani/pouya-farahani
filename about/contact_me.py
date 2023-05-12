from django.contrib import messages
from django.shortcuts import render

from .forms import CommentForm


def contact_me_form(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "نظر شما با موفقیت ثبت شد")
    else:
        messages.warning(request, f"لطفا اطلاعات را به درستی وارد کنید")
        return render(request, 'home/home.html')
