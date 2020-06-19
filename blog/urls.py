from django.urls import path
from . import views

urlpatterns = [
    path('/posts', views.IndexView.as_view(), name='post_list'),
    path('/new', views.CreateView.as_view(), name='post_form'),
    # path('posts', views.IndexView.as_view(), name='post_list'),
    # path('posts', views.IndexView.as_view(), name='post_list'),
]