from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import LoginForm, UserDataUpdateForm, RegisterForm

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

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'User_App/profile_page.html'
    # further implementation needed.
    
    