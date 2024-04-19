from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *

# Create your views here.
class PostsList(ListView):
    model = Post
    template_name = 'posts_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    queryset = Post.objects.all().order_by('-date_in')

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})