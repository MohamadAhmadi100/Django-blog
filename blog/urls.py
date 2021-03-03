from .views import (blog_home,
                    blog_about,
                    PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    )
from django.urls import path

urlpatterns = [
    # path('', blog_home, name="blog_home"),
    path('', PostListView.as_view(), name="blog_home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user_posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('about/', blog_about, name="blog_about")
]
