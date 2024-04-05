from django.contrib import admin
from .models import Drone, Medication,BatteryAuditLog

admin.site.register(Drone)
admin.site.register(Medication)
admin.site.register(BatteryAuditLog)