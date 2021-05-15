from sympy import *
x = Symbol('x')


#takes in an equation for displacement as a string and derives it to find velocity
def differentiate(your_equation):
    your_equation = your_equation.replace("^", "**")
    f_prime = diff(your_equation)
    f_prime = str(f_prime)
    if "x" not in f_prime:
        f_prime = 'y=' + f_prime
    f_prime = f_prime.replace("**", "^")

    return f_prime

#takes in an equation for displacement as a string and double derives it to find acceleration
def doubleDifferentiate(your_equation):
    your_equation = your_equation.replace("^", "**")
    f_double_prime = diff(your_equation, x, x)
    f_double_prime = str(f_double_prime)
    if "x" not in f_double_prime:
        f_double_prime = 'y=' + f_double_prime
    f_double_prime = f_double_prime.replace("**", "^")
    return f_double_prime

def integ(your_equation):
    your_equation = your_equation.replace("^", "**")
    integral = integrate(your_equation, x)
    integral = str(integral)
    if "x" not in integral:
        integral = 'y=' + integral
    integral = integral.replace("**", "^")
    return integral

def doubleInteg(your_equation):
    integral = integ(your_equation)
    double_integral = integ(integral)
    return double_integral