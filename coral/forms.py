from django import forms
from django.forms import ModelForm
from .models import Coral

class DateInput(forms.DateInput):
        input_type = 'date'
        
class CoralForm(forms.ModelForm):

    

    class Meta:
        model = Coral
        fields = ["name", "description", "status" , "source", "purchaseDate","purchaseCost","image"]
        widgets = {
            'purchaseDate': DateInput(),
        }

