from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('room/<str:pk>/', views.room, name='room'),  # Room page with dynamic ID

    path('create-Room/',views.createRoom ,name ="create-room")
    path('update-Room/<>/',views.updateRoom ,name ="update-room")
]
