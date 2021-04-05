from django.urls import path

from . import views
from .forms import EquationForm

urlpatterns = [
    path('', views.graph),

]