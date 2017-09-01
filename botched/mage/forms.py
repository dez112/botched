from django import forms

class NpcSearchForm(forms.Form):
    name = forms.CharField(max_length=200, help_text="who are you looking for?")