
from django.db import models

#The actual fragrance/cologne
class Fragrance(models.Model):
	brand = models.CharField(max_length = 100, default = '')
	name = models.CharField(max_length = 100)
	review = models.CharField(max_length = 500)
	rating = models.FloatField()
	image = models.ImageField(upload_to='images/', blank = True)
	@property
	def image_url(self):
		if self.image:
			return self.image.url
		else: 
			self.image = "C:/Users/Evan/Desktop/Django_blog_site/django_blog_site/django_blog_site/media/unknown.png"
			return self.image.url


	def __str__(self):
		return self.name

#Intermediate between Personal Favorites cart and individual Fragrance
class Fragrance_Favorite(models.Model):
	fragrance = models.ForeignKey(Fragrance, on_delete = models.CASCADE)

	def __str__(self):
		return self.title

#Like a shopping cart, ideally a 'personal fav' list for each occasion/season
class PersonalFavorites(models.Model):
	items = models.ManyToManyField(Fragrance_Favorite)
	favorite = models.BooleanField(default = False)


	def __str__(self):
		return self.title