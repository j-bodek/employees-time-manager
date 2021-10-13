from django.urls import path
from . import views

urlpatterns = [
    path('get_csv', views.get_csv, name='get_csv'),
    path('stats', views.display_charts, name='display_charts'),
    path('table', views.employees_table, name='employees_table'),
   
]