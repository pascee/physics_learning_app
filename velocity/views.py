from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EquationForm
from . import calculations

#from json import dumps

# Create your views here.
#very basic render request that displays the desmos.html page
def graph(request, your_equation = 'x'):
    if request.method == 'POST':
        form = EquationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            your_equation = data['equation_input']

    else: 
        form = EquationForm()

    velocity = calculations.differentiate(your_equation)
    acceleration = calculations.doubleDifferentiate(your_equation)

    context = {
        'your_equation' : your_equation,
        'form' : form,
        'velocity' : velocity,
        'acceleration' : acceleration,
    }
            

    return render(request, 'velocity/FinalDesmos.html', context)

