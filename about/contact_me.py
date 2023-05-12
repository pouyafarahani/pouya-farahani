from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from .forms import CommentForm


@require_http_methods(["POST"])
def contact_me_form(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "نظر شما با موفقیت ثبت شد")
    else:
        messages.warning(request, f"لطفا اطلاعات را به درستی وارد کنید")
    return redirect('home')
