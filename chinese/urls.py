from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_character, name='add'),
    path('practice/', views.practice, name='practice'),
    path('stats/', views.stats, name='stats'),
]
