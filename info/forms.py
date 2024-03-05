from django.forms import ModelForm

from .models import Information

class InformationForm(ModelForm):
    
    class Meta:
        model = Information
        fields = ['name', 'age', 'email', 'job']