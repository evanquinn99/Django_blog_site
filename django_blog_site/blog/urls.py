from django.urls import path
from . import views

urlpatterns = [
	path('', views.fragrance_list, name = 'fragrance_list'),
    path('home/', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]