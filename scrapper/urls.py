from django.urls import path
from . import views

app_name = 'scrapper'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
]
