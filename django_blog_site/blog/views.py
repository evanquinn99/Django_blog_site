from django.shortcuts import render
from django.http import HttpResponse
from .models import Fragrance

def fragrance_list(request):
	context = {
		'fragrances' : Fragrance.objects.all()
	}
	return render(request, 'blog/fragrance_list.html', context)

def home(request):
	return render(request, 'blog/home.html')

def about(request):
	return render(request, 'blog/about.html') 