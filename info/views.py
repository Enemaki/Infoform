from django.views.generic import CreateView, TemplateView
from django.urls import reverse

from .forms import InformationForm

class HomePageView(TemplateView):
    template_name = 'home.html'
        
class InformationFormView(CreateView):
    form_class = InformationForm
    template_name = 'info.html'
    def get_success_url(self):
        return reverse('success')
    
class SuccessView(TemplateView):
    template_name = 'success.html'