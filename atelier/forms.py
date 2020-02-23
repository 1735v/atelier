from django import forms

class EmailPostForms(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    #telefonnumber=forms.NumberInput()
    message = forms.CharField(widget=forms.Textarea)
