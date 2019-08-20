from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blog.models import BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost
    context_object_name = 'blogpost'
    template_name = 'blog/blog_detail.html'


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blogpostlist'
    template_name = 'blog/blog_list.html'
    queryset = BlogPost.objects.filter(published=True)
