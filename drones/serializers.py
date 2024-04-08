from rest_framework import serializers
from .models import Drone
from .models import Medication


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ['id', 'serial_number', 'model', 'weight_limit', 'battery_capacity', 'state']


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'name', 'weight', 'code', 'image']


class DroneLoadedSerializer(serializers.ModelSerializer):
    medication = serializers.SerializerMethodField()

    class Meta:
        model = Drone
        fields = ['serial_number', 'weight_limit', 'battery_capacity', 'state', 'medication']

    def get_medication(self, obj):
        medications = obj.medication.all()
        return MedicationSerializer(medications, many=True).data
