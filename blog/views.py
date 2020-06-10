from django.shortcuts import render
from blog.models import Post
# Create your views here.

def post_list(request):
    posts= Post.objects.all()
    return render(request, 'blog/post_list.html', {
         "posts":posts
    })
from .forms import PostForm
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
