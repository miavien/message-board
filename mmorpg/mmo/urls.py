from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostsList.as_view(), name='posts_list'),
]