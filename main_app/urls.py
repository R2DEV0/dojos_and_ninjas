from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('show', views.show),
    path('submit_ninja', views.submit_ninja),
    path('submit_dojo', views.submit_dojo),
    ]