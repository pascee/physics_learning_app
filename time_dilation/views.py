from django.shortcuts import render

# Create your views here.

def time_dilation(request):
    return render(request, 'time_dilation.html')