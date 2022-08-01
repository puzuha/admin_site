from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('maps', views.maps, name='map'),
    path('create', views.create, name='create'),

]
