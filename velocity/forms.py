from django import forms

class EquationForm(forms.Form):
    your_equation = forms.CharField(label = 'Your Equation', max_length = 100)