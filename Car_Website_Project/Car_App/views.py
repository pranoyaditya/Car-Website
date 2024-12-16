from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .models import Car
from User_App.models import PurchasedCar
from .forms import CommentForm

# Create your views here.
class CarDetails(DetailView):
    template_name = 'Car_App/car_details.html'
    model = Car

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car_post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car_post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        car_post = self.object 
        comments = car_post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form

        return context


class BuyCarView(LoginRequiredMixin, View):
    def post(self, request, car_id, *args, **kwargs):
        # Get the car object
        car = Car.objects.get(id = car_id)

        if car.quantity > 0:
            # Reduce car quantity
            car.quantity -= 1
            car.save()

            # Add to PurchasedCar
            PurchasedCar.objects.create(user=request.user, car=car)

            messages.success(request, f"You have successfully purchased {car.car_name}.")
        else:
            messages.error(request, "Sorry, this car is out of stock!")

        return redirect('home_page')
