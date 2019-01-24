from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pub_date')
    paginator = Paginator(posts, 2)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def show(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('show', post_id=post.id)
    else:
        form = CommentForm()     
    
    comments = Comment.objects.filter(post=post_id)
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(request, 'blog/show.html', context)
