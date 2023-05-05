# Import necessary modules
from django.views.generic import DetailView, ListView
from home.views import BlogModel

# Define list view for the blog model
class BlogListView(ListView):
    # Set template used to render the list view
    template_name = 'blog/blog_list.html'
    # Set the model used to fetch data in the list view
    model = BlogModel
    # Name of the context object passed to the template
    context_object_name = 'blog'
    # Number of items to display per page
    paginate_by = 6

# Define detail view for the blog model
class BlogDetailView(DetailView):
    # Set template used to render the detail view
    template_name = 'blog/blog_detail.html'
    # Set the model used to fetch data in the detail view
    model = BlogModel
    # Name of the context object passed to the template
    context_object_name = 'blog'
