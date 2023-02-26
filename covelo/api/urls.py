
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('locker/<str:locker_id>/', views.locker_detail, name='locker'),
    path('bicycle/<int:pk>/', views.BicycleDetailView.as_view(),
         name='bicycle_detail'),
    path('bicycle/unlock', views.Unlock_Bicycle, name='unlock_bicycle'),
    path('bicycle/lock', view=views.Lock_Bicycle, name='lock-bicycle')
]
