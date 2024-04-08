from celery import shared_task
from datetime import datetime
from .models import Drone, BatteryAuditLog

@shared_task
def check_battery_levels():
    print(":logging battery level")
    drones = Drone.objects.all()
    for drone in drones:
        BatteryAuditLog.objects.create(drone=drone, battery_level=drone.battery_capacity)
    print(":Battery levels logged")