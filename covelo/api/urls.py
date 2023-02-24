
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('bicycle_info/', views.get_bicycle_info, name='bicycle_info'),
]
