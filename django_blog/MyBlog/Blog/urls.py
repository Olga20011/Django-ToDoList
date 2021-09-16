from . import views
from django.urls import path
from .views import Post_list,Post_detail



urlpatterns=[
    path('',Post_list.as_view(), name='home'),
    path('', Post_detail.as_view(),name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail')

]