from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login_ac,name='login_ac'),
    path('register/',views.register, name='register'),
    path('Home/',views.home, name='home'),
]
