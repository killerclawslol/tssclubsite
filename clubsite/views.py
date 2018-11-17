from django.shortcuts import render
from .models import Post
from .models import Name
def home(request):
    context = {
        'name': Name.objects.all()
    }
    return render(request, 'home.html', context)
def news(request):
    context = {
        'post': Post.objects.all(),
        'name': Name.objects.all()
    }
    return render(request, 'news.html', context)
