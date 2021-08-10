from django.urls import path
from . import views

urlpatterns=[
    path("register/",views.index,name="list"),
    path("update_task/<int:primary_key>/", views.update_task,name="update"),
    path("delete/<int:pk>/",views.deleteTask,name="delete")
]
