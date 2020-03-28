from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import TemplateView
from .models import Fragrance
from blog.forms import CreateForm
from django.contrib import messages


class CreateView(TemplateView):
	template_name = 'blog/create.html'

	def get(self, request):
		form = CreateForm()
		return render(request, self.template_name, {'form' : form})

	def post(self,request):
		form = CreateForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			messages.success(request, f'Your fragrance has been added.')
			return redirect('fragrance_list')

		else:
			return HttpResponseBadRequest(str(form.errors))

		args = {'form': form}
		return render(request, self.template_name, args)




def fragrance_list(request):
	context = {
		'fragrances' : Fragrance.objects.all()
	}
	return render(request, 'blog/fragrance_list.html', context)

def fragrance_detail(request, pk):
    fragrance = Fragrance.objects.get(pk=pk)
    context = {
        'fragrance': fragrance
    }
    return render(request, 'blog/fragrance_detail.html', context)	

def home(request):
	return render(request, 'blog/home.html')
def about(request):
	return render(request, 'blog/about.html') 