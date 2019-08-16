from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blogs.models import Blog


class BlogPostDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BlogPostListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    queryset = Blog.objects.filter(published=True)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
