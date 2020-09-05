from django.urls import path

from . import views

app_name = 'crew_tracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_ship/', views.create_ship, name="create_ship"),
    path('ships/', views.ship_index, name='ship_index')
]

