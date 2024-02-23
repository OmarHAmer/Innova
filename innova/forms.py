from django import forms
from .models import *

class FormSuggestions(forms.ModelForm):
    class Meta:
        model = Suggestions
        fields = ['Full_Name','Email_address','Phone','Message']


class FormCareer(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name','telephone','email','address','state','city','jobVacancy','attachCV']

    