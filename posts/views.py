from django.shortcuts import render

def post(request):  # temporary for styling
    return render(request, 'posts/post.html')
