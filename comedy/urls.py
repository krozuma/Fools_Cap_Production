from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/<int:art_id>/', views.detail, name='detail'),
    #re_path(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$', views.detail, name='detail'),
    path('news/', views.news, name='news'),
    path('politics/', views.politics, name='politics'),
    path('local/', views.local, name='local'),
    path('sports/', views.sports, name='sports'),
    path('opinion/', views.opinion, name='opinion'),
    path('health/', views.health, name='health'),
    path('entertainment/', views.entertainment, name='entertainment'),
]
