from django.http import FileResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
# Create your views here.


def committee(request):
    if request.method == 'GET':
        return render(request, 'committee.html')


def achievements(request):
    if request.method == 'GET':
        return render(request, 'achievements.html')


def blog(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        paginator = Paginator(posts, 2)
        page_number = request.GET.get('page', 1)
        print('no of pages {0}'.format(paginator.num_pages))
        try:
            posts = paginator.page(page_number)
        except EmptyPage:
            posts = paginator.page(1)
        return render(request, 'blog.html', {'posts': posts})


def index(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'index.html', {'posts': posts})


def post(request, val):
    post = Post.objects.get(id=val)
    try:
        next_post = Post.objects.get(id=int(val)+1)
    except:
        next_post = None
    try:
        last_post = Post.objects.get(id=int(val)-1)
    except:
        last_post = None
    return render(request, 'post.html', {'post': post, 'last_post': last_post, 'next_post': next_post, })


def images(request, img):

    img = open(f'images/{img}', 'rb')

    return FileResponse(img)
