from django.contrib import admin
from .models import Fragrance, Fragrance_Favorite, PersonalFavorites


# Register your models here.
admin.site.register(Fragrance)
admin.site.register(Fragrance_Favorite)
admin.site.register(PersonalFavorites)