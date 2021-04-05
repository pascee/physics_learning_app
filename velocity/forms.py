from django import forms

TYPES_OF_EQUATIONS = [
    ('displacement', 'Displacment'),
    ('velocity', 'Velocity'),
    ('acceleration', 'Acceleration'),
]
class EquationForm(forms.Form):
    equation_input = forms.CharField(label = 'Your Equation', max_length = 100)
    """equation_type = forms.MultipleChoiceField(
        
        widget=forms.RadioSelect,
        choices=TYPES_OF_EQUATIONS
    )"""