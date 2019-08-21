from django.views.generic import ListView

from blog.models import BlogPost


class HomeView(ListView):
    context_object_name = 'topposts'
    template_name = 'index.html'

    def get_queryset(self):
        # Get the latest 3 blogs
        queryset = BlogPost.objects.filter(published=True).order_by('-published_date')
        return queryset[:3]
