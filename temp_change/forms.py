from django import forms


class my_form(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "enter your name" }))
    latname = forms.CharField()
    email = forms.EmailField()
