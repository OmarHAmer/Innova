from django import forms
from account.nodeModels.navBar import NavBar

class FormNavBar(forms.ModelForm):
    class Meta:
        model = NavBar
        fields = ['title','child_list_flag','parent','order_by','active_flag']

