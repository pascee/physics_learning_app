from django.shortcuts import render

# Create your views here.

def new_user_menu(request):
    return render(request, 'new_user_menu.html')

