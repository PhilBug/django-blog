from django.shortcuts import render
# from django.http import HttpResponse

from posts.models import Post

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
