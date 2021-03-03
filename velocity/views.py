from django.shortcuts import render
from sympy import *
x = Symbol('x')

# Create your views here.
#very basic render request that displays the desmos.html page
def graph(request):
    return render(request, 'velocity/desmos.html',)


#idk if these methods are made correctly or if they should be in this file
#takes in an equation for displacement as a string and derives it to find velocity
def velociterize(String):
    f = String
    f_prime = f.diff(x)
    # not sure if this acutally works like i think it does so maybe remove and instead in the =x before entering into the graph
    f_prime = lambdify(x,f)

    return f_prime

#takes in an equation for displacement as a string and double derives it to find acceleration
def acceleterize(String):
    f = String
    f_prime = f.diff(x)
    f_double_prime = f_prime.diff(x)
   # not sure if this acutally works like i think it does so maybe remove and instead in the =x before entering into the graph
    f_double_prime = lambdify(x,f)
    
    return f_double_prime