from django.urls import path
from blog import views
from blog.views import AddTopicView, AddPostView, CreateCommentView, PostDetailView

urlpatterns = []

urlpatterns += [
    path('', views.get_topics, name='topics'),
    path('posts/<int:pk>', views.get_topic_posts, name='posts'),
    path('create_topic/', AddTopicView.as_view(), name='create_topic'),
    path('posts/add_post/', AddPostView.as_view(), name='add_post'),
    path('like-post/<int:pk>/', views.like_view, name='like_post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/create_comment', CreateCommentView.as_view(), name='create_comment'),
    path('register', views.register_request, name='register'),
    path("login", views.login_request, name="login"),
]
