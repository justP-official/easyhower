from django.urls import path
from django.contrib.auth.views import LogoutView

from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('logout/', LogoutView.as_view(), name='logout'),
]