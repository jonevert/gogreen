from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/overview
    path('', views.index, name="overview-index"),
]
