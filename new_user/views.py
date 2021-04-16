from django.shortcuts import render

# Create your views here.

def new_user_initial_menu(request):
    return render(request, 'new_user_initial_menu.html')



def main_page(request):
    return render(request, 'mainPage.html')
