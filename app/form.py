from  django.forms import ModelForm
from .models import Todoapp

class TodoAppForm(ModelForm):
    class Meta:
        model= Todoapp
        fields='__all__'