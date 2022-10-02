from django.urls import path
from cars_catalog.views import list

urlpatterns = [
    path('', list, name="list")
]
