from django import forms
from .models import Fragrance

class CreateForm(forms.ModelForm):
	"""brand = forms.CharField()
	name = forms.CharField()
	review = forms.CharField()
	rating = forms.FloatField()
	image = forms.ImageField(required=False)"""
	class Meta:
		model = Fragrance
		image = forms.ImageField(required=False)
		fields = ['brand', 'name', 'review', 'rating', 'image']
