from django.shortcuts import render


# Create your views here.
#very basic render request that displays the desmos.html page
def graph(request):
    return render(request, 'velocity/desmos.html',)


