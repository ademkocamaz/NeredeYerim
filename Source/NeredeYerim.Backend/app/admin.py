from django.contrib import admin

# Register your models here.
from app.models import City, Restaurant, Food

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in City._meta.fields if field.name not in ("id")]
    list_display_links = [field.name for field in City._meta.fields if field.name not in ("id")]
    search_fields = [field.name for field in City._meta.fields if field.name not in ("id")]

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Restaurant._meta.fields if field.name not in ("id")]
    list_display_links = [field.name for field in Restaurant._meta.fields if field.name not in ("id")]
    search_fields = [field.name for field in Restaurant._meta.fields if field.name not in ("id")]
    

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.fields if field.name not in ("id")]
    list_display_links = [field.name for field in Food._meta.fields if field.name not in ("id")]
    search_fields = [field.name for field in Food._meta.fields if field.name not in ("id")]