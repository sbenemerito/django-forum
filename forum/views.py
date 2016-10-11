from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User


def index(request):
    posts = Post.objects.all().order_by('-date_added')
    phixen = User.objects.get(id=1)
    tops = Post.objects.filter(author=phixen)
    context = {'posts': posts, 'tops': tops}

    return render(request, 'forum/index.html', context)


def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.all()
    comment_count = post.comment_set.count()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('forum:post', args=[post.id]))
    else:
        form = CommentForm()

    context = {'post': post, 'comments': comments, 'comment_count': comment_count, 'form': form}
    return render(request, 'forum/post.html', context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('forum:post', args=[post.id]))
    else:
        form = PostForm(instance=post)

    context = {'post': post, 'form': form}
    return render(request, 'forum/edit_post.html', context)


def new_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('forum:post', args=[post.id]))
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'forum/new_post.html', context)


def user_view(request, user_name):
    user = get_object_or_404(User, username=user_name)
    user_posts = Post.objects.filter(author=user)
    context = {'userprofile': user, 'posts': user_posts}
    return render(request, 'forum/user.html', context)
