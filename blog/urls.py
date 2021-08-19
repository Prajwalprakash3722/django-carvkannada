from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('committee', views.committee, name='committee'),
    path('achievements', views.achievements, name='achievements'),
    path('blog', views.blog, name='blog'),
    path('post/<str:val>', views.post, name='post'),
    path('post/images/<str:img>', views.images, name='images'),
    path('images/<str:img>', views.images, name='images')
]
