from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EquationForm
from . import calculations

#from json import dumps

# Create your views here.
def graph(request):
    your_equation = 'x'
    equation_type = 'Displacement'
    displacement = 'x'
    velocity = '1'
    acceleration = '0'
    if request.method == 'POST':
        form = EquationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            your_equation = data['equation_input']
            equation_type = data['equation_type']

            
        if equation_type == 'Displacement':
            displacement = your_equation
            velocity = calculations.differentiate(your_equation)
            acceleration = calculations.doubleDifferentiate(your_equation)

        elif equation_type == 'Velocity':
            displacement = calculations.integ(your_equation)
            velocity = your_equation
            acceleration = calculations.differentiate(your_equation)

        elif equation_type == 'Acceleration':
            displacement = calculations.doubleInteg(your_equation)
            velocity = calculations.integ(your_equation)
            acceleration = your_equation

        else:
            displacement = '-1'
            velocity = '-1'
            acceleration = '-1' 
            
            

    else: 
        form = EquationForm()




    

    context = {
        'your_equation' : your_equation,
        'form' : form,
        'displacement' : displacement,
        'velocity' : velocity,
        'acceleration' : acceleration,
    }
            

    return render(request, 'velocity/FinalDesmos.html', context)

