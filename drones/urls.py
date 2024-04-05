from django.contrib import admin
from django.urls import path
from drones import views

urlpatterns = [
    path('register/drone', views.RegisterDroneView.as_view(), name='register_drone'),
    path('add/medication', views.AddMedicationView.as_view(), name='add_medication'),
    path('load/medication', views.LoadDroneView.as_view(), name='load_drone_medication'),
    path('drone/medication/<str:drone_serial_number>/', views.GetLoadedMedicationView.as_view(),
         name='get_loaded_medication'),
    path('available-drones/', views.GetAvailableDronesView.as_view(), name='get_available_drones'),
    path('battery/<str:drone_serial_number>/', views.GetBatteryLevelView.as_view(), name='get_battery_level'),
]
