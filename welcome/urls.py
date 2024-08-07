from django.urls import path

from welcome import views

app_name = 'welcome'

urlpatterns = [
    path('', views.WelcomeIndex.as_view(), name='index'),
]