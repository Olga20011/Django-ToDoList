from . import views
from django.urls import path
from .views import Post_list,Post_detail



urlpatterns=[
    path('',Post_list.as_view(), name='home'),
    path('<slug:slug>/', Post_detail.as_view(),name='post_detail'),
]