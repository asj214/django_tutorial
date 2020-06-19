from django.views.generic import ListView, FormView, DetailView
from .models import Post


class IndexView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class CreateView(FormView):
    template_name = 'blog/post_form.html'
    context_object_name = 'posts'