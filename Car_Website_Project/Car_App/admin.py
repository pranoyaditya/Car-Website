from django.contrib import admin
from .models import Car, Brand, Comment

# Register your models here.
admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Comment)

class carAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'brand_name', 'slug')
    prepopulated_fields = {'slug' : ('car_name', )}
