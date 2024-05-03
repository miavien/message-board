from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from django_filters import FilterSet
from .tasks import send_notify_new_post

from .models import *
from .forms import *

class PostFilter(FilterSet):
    class Meta:
        model = Response
        fields = [
            'post'
        ]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostFilter, self).__init__(*args, **kwargs)
        if user:
            self.filters['post'].queryset = Post.objects.filter(user=user)
        if not self.data:
            self.queryset = Response.objects.none()


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

class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        post = form.save(commit=False)
        post.save()
        # send_notify_new_post.delay(post.pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})


class PostUpdate(LoginRequiredMixin, UpdateView):
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
        context['category'] = category
        context['is_not_subscriber'] = self.request.user not in category.subscribers.all()
        context['category_name'] = category_dict.get(category.name, category.name)
        return context

def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    return render(request, 'subscribe_success.html')

class Personal(LoginRequiredMixin, TemplateView):
    template_name = 'pesonal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Response.objects.filter(user=self.request.user)
        context['filterset'] = PostFilter(self.request.GET, queryset=queryset)
        return context

def accept_response(request, response_id):
    response = get_object_or_404(Response, pk=response_id)
    if request.user.is_authenticated and request.user == response.post.user:
        response.status = True
        response.save()
    return redirect(reverse('personal'))

def deny_response(request, response_id):
    response = get_object_or_404(Response, pk=response_id)
    if request.user.is_authenticated and request.user == response.post.user:
        response.delete()
    return redirect(reverse('personal'))

class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'invalid_code.html')
        return redirect('login')