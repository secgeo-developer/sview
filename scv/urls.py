
from django.urls import path
from scv import views


urlpatterns = [
    # Define your URL patterns here
    path('', views.index, name='starting-page'),
]
