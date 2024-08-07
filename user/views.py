from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.models import Task
from user.forms import UserLoginForm, UserPasswordChangeForm, UserRegistrationForm

# Create your views here.

class UserLogin(LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    extra_context = {'title': 'Easyhower - Войти',}


class UserRegistration(CreateView):
    template_name = 'user/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user:profile')
    extra_context = {'title': 'Easyhower - Регистрация',}



class UserProfile(LoginRequiredMixin, ListView):
    template_name = 'user/profile.html'
    context_object_name = 'tasks'
    extra_context = {"title": "Easyhower - Профиль",}

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user, is_active=False)


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('user:profile')
