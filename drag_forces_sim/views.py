from django.shortcuts import render

from .models import DragObject

def index(request):
    
    return render(request, 'dragSimMainPage/dragSimMainPage.html')

