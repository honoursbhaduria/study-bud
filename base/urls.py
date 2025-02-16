from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    path('login/' , views.loginPage , name="login"),
    path('logout/' , views.logoutUser , name="logout"),
    path('register/' , views.registerPage , name="register"),

    path('', views.home, name='home'),  # Home page
    path('room/<str:pk>/', views.room, name='room'),  # Room page with dynamic ID

    path('createRoom/',views.createRoom ,name ="create-room"),
    path('updateRoom/<str:pk>/',views.updateRoom ,name ="update-room"),
    path('deleteRoom/<str:pk>/',views.deleteRoom ,name ="delete-room")
    
]
