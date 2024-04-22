from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response_form'] = ResponseForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.post = post
            response.user = request.user
            response.save()
            return redirect('post', pk=post.pk)

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


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})

class CategoryList(PostsList):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_posts_list'
    def get_queryset(self):
        category_pk = self.kwargs['category_pk']
        return Post.objects.filter(category_id=category_pk).order_by('-date_in')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_pk']
        category = get_object_or_404(Category, pk=category_id)
        category_dict = dict(Category.CATEGORY_TYPES)
        context['category_name'] = category_dict.get(category.name, category.name)
        return context