from django.contrib import admin
from django.urls import path
from drones import views

urlpatterns = [
    path('drones/register', views.RegisterDroneView.as_view(), name='register_drone'),
    path('add/medication', views.AddMedicationView.as_view(), name='add_medication'),
    path('view/medication', views.GetMedicationView.as_view(), name='get_medication'),
    path('drones/load', views.LoadDroneView.as_view(), name='load_drone_medication'),
    path('drones/loaded/<str:drone_serial_number>/', views.GetLoadedMedicationView.as_view(),
         name='get_loaded_medication'),
    path('drones/available', views.GetAvailableDronesView.as_view(), name='get_available_drones'),
    path('drones/battery/<str:drone_serial_number>/', views.GetBatteryLevelView.as_view(), name='get_battery_level'),
]
