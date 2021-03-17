from django.urls import path

from . import views

urlpatterns = [
    path('', views.graph),
    path('graph/', views.get_equation),
    path('graph/<str:your_equation>/', views.graph, name = 'graph'),
    path('graph/redirect', views.goToGraph)
]