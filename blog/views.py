from django.shortcuts import get_object_or_404, render
from blog.models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.all().order_by('sold_amount')
    return render(request, 'blog/post_list.html', {
        "posts": posts
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {
        "post": post
    })
