from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostsList.as_view(), name='posts_list'),
    path('post/<int:pk>', PostDetail.as_view(), name='post'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
]