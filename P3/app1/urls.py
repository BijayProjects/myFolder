from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,{'status':'App1'}),
    path('home/',views.home),
]