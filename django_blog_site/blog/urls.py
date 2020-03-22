from django.urls import path
from . import views

urlpatterns = [
	path('', views.fragrance_list, name = 'fragrance_list'),
	path("<int:pk>/", views.fragrance_detail, name="fragrance_detail"),
    path('home/', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]