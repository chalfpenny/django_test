from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    street = forms.CharField(label="Street", max_length=50)