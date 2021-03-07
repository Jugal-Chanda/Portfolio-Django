from django.urls import path
from blog import views


urlpatterns = [
    path('', views.index, name='blog.index'),
    path('create/', views.create, name='blog.create'),
    path('deleteblog/<int:id>',views.delete,name="blog.delete"),
]
