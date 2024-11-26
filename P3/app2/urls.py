from django.urls import path
from .import views

urlpatterns = [
    path('app2/',views.home),
    path('app2home/',views.home,{'status':'App2'}),
]