# Import necessary modules
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from blog.models import BlogModel
from .forms import CommentForm

# Define view for the home page
def home_view(request):
    
    # Query set of 3 latest blog posts with related objects extracted
    queryset = BlogModel.objects.order_by('-id')[:3].select_related()
    
    # Store query set in context dictionary
    context = {'blog': queryset}

    # If user submits a form to add a comment
    if request.method == 'POST':
        
        # Create an instance of CommentForm with submitted data
        form = CommentForm(request.POST)
        
        # If form is valid, save it and show success message
        if form.is_valid():
            form.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد')
            
        # If form is invalid, show warning message
        else:
            messages.warning(request, f'لطفا اطلاعات را به درستی وارد کنید')

        # Redirect to the home page
        return redirect(reverse_lazy('home:home'))

    # If not POST request, show home page with stored context dictionary
    return render(request, 'home/home.html', context)
