from django import forms
from django.forms import TextInput
from .models import *


class user_status(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(user_status, self).__init__(*args, **kargs)
    class Meta:
        model = user_details
        fields = ['name','age','mail_id','gender','image1','image2']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'enter your name'
                }),
            'age': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 100px;',
                'placeholder':'your age'
                }),
            'mail_id': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'enter your mail id'
                }),
        }
        