from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand_name}'

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    car_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_details = models.TextField()
    quantity = models.IntegerField()
    car_image = models.ImageField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.car_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.car_name} ({self.brand})"
       
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.car.name}"
