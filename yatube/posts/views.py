from django.shortcuts import get_object_or_404, render
from .models import Group, Post

NUM_OF_PUBLICATIONS: int = 10


def index(request):
    posts = Post.objects.all()[:NUM_OF_PUBLICATIONS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUM_OF_PUBLICATIONS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
