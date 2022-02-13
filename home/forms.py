from .models import files
from django import forms
from django.forms import ModelForm
class filesform(ModelForm):
    fil = forms.FileField(widget=forms.ClearableFileInput(attrs={"class": "xyz"}))
    class Meta:
        model = files
        fields = ['fil']