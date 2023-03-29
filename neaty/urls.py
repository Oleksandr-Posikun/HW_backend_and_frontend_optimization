from django.urls import path
from neaty.views import index

urlpatterns = [
    path('', index),
    ]
