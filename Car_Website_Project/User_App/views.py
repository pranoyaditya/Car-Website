from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import LoginForm, UserDataUpdateForm, RegisterForm
from .models import PurchasedCar

# Create your views here.
class SignUpView(UserPassesTestMixin, CreateView):
    template_name = 'User_App/signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login_page')

    def test_func(self):
        # prevents authenticated users to view this page.
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        # returns authenticated users to home page.
        return redirect('home_page')

    def form_valid(self, form):
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'User_App/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        return super().form_valid(form)
    
class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home_page')

    def handle_no_permission(self):
        # redirects non-logged in users to login page.
        return redirect('login_page')

class ProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'User_App/profile_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchased_cars = PurchasedCar.objects.filter(user=self.request.user).select_related('car')
        context['purchased_cars'] = purchased_cars
        return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'User_App/update_profile.html'
    form_class = UserDataUpdateForm
    success_url = reverse_lazy('profile_page')

    def get_object(self, queryset=None):
        # Return the currently logged-in user
        return self.request.user
    