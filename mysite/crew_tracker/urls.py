from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

app_name = 'crew_tracker'
urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='crew_tracker/index.html'), name="home"),
    path('ships/', views.ShipIndex.as_view(), name='ship_index'),
    path('ships/<int:pk>/details', views.ShipDetails.as_view(), name='ship_details'),
    path('create_ship/', views.create_ship, name="create_ship"),
    path('create_crewman/', views.create_crewman, name="create_crewman"),
    path('create_crewman/<int:ship_id>', views.create_crewman, name="assign_crewman"),
]

