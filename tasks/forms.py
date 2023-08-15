from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['tittle', 'descripcion', 'important']
        widgets= {
            'tittle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribir titulo'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Escribir la descripcion'}),
          'important': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }