from django.urls import path
from . import views

urlpatterns = [
    path("w_map/", views.w_map, name="w_map"),
    # path("a_map/", views.a_map, name="a_map"),
]