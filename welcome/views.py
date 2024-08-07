from django.views.generic import TemplateView

# Create your views here.

class WelcomeIndex(TemplateView):
    template_name = 'welcome/index.html'
    extra_context = {'title': 'Easyhower - Главная'}