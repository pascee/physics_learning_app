from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EquationForm

#from json import dumps

# Create your views here.
#very basic render request that displays the desmos.html page
def graph(request, your_equation):
    context = {
        'your_equation' : your_equation
        }
    return render(request, 'velocity/desmos.html', context)

def get_equation(request):
    if request.method == 'POST':
        form = EquationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else: 
        form = EquationForm()
        
    return render(request, 'velocity/equation_intake.html', {'form': form})

def goToGraph(request):
    return HttpResponseRedirect('velocity/graph/<your_equation>')
    
