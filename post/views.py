from django.views.generic import ListView
from post.models import Post

class PostListView(ListView):
    
    model = Post
    template_name = 'home.html'
    context_object_name='posts'
