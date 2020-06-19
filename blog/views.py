from django.views.generic import ListView, CreateView, DetailView
from .models import Post
# from .forms import PostForm

class IndexView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class PostFormView(CreateView):
    template_name = 'blog/post_form.html'
    # form_class = PostForm
