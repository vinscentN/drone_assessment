from django.core.management.base import BaseCommand
from drones.models import Drone, BatteryAuditLog
from django.utils import timezone

class Command(BaseCommand):
    help = 'Check drone battery levels and create audit logs'

    def handle(self, *args, **kwargs):
      
        drones = Drone.objects.all()
        for drone in drones:
            battery_level = drone.battery_capacity
            BatteryAuditLog.objects.create(drone=drone, battery_level=battery_level, created_at=timezone.now())
            self.stdout.write(self.style.SUCCESS(f"Created BatteryAuditLog for drone {drone.serial_number} with battery level {battery_level}%"))