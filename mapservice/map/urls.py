from django.urls import path
from . import views

urlpatterns = [
    path("w_map/", views.w_map, name="w_map"),
    path("getApi/", views.getApi, name='getApi'),
    path("mapTest/", views.mapTest, name='mapTest'),
]