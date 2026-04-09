from django.urls import path
from . import views

urlpatterns = [
    path('', views.nexus_index, name='index'),
    path('transcendence/', views.transcendence, name='transcendence'),
    path('bioelectric/', views.bioelectric, name='bioelectric'),
    path('touchless/', views.touchless, name='touchless'),
    path('biomimicry/', views.biomimicry, name='biomimicry'),
]
