from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
class PostsList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'posts_list.html'
    context_object_name = 'posts'
    paginate_by = 20