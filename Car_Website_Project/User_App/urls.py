from django.urls import path
from .views import UserLoginView, SignUpView, ProfileView, UserLogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup_page'),
    path('login/', UserLoginView.as_view(), name='login_page'),
    path('logout/', UserLogoutView.as_view(), name='logout_page'),
    path('profile/', ProfileView.as_view(), name='profile_page'),
]