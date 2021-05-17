from django import forms

TYPES_OF_EQUATIONS = [
    ('Displacement', 'Displacment'),
    ('Velocity', 'Velocity'),
    ('Acceleration', 'Acceleration'),
]
class EquationForm(forms.Form):
    equation_input = forms.CharField(label = 'Your Equation', max_length = 100)
    equation_type = forms.ChoiceField(
        
        widget=forms.RadioSelect,
        choices=TYPES_OF_EQUATIONS
    )