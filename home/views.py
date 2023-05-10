# Import necessary modules
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from blog.models import BlogModel
from .forms import CommentForm


def home_view(request):

    queryset = BlogModel.objects.order_by('-id')[:3].select_related()
   
    context = {'blog': queryset}

    if request.method == 'POST':
        

        form = CommentForm(request.POST)
        

        if form.is_valid():
            form.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد')

        else:
            messages.warning(request, f'لطفا اطلاعات را به درستی وارد کنید')


        return redirect(reverse_lazy('home:home'))

    return render(request, 'home/home.html', context)
