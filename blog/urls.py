from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='post_list'),
    path(r'create', views.PostFormView.as_view(), name='post_form')
]