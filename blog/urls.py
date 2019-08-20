from django.urls import path

from blog.views import BlogPostDetailView, BlogPostListView


urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-list'),
    path('<int:pk>', BlogPostDetailView.as_view(), name='blog-detail'),
]
