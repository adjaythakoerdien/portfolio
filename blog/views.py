from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def home(request):
#     return render(request, 'blog_posts.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'blog_posts.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
