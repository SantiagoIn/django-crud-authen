from django.forms import ModelForm
from django import forms
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=['title','description','important']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Task Title'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'important':forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }