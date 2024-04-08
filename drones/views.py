from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Drone, Medication
from .serializers import DroneSerializer, MedicationSerializer, DroneLoadedSerializer


def generate_response(status_code, message, data):
    response_data = {
        'statusCode': status_code,
        'message': message,
        'data': data
    }
    return Response(response_data, status=status_code)


class RegisterDroneView(APIView):
    def post(self, request):
        serializer = DroneSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except ValidationError as e:
                return generate_response(status.HTTP_400_BAD_REQUEST, 'Bad Request', str(e))
            return generate_response(status.HTTP_201_CREATED, "Drone Successfully added", serializer.data)
        return generate_response(status.HTTP_400_BAD_REQUEST, 'Bad Request', serializer.errors)


class AddMedicationView(APIView):
    def post(self, request):
        serializer = MedicationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except ValidationError as e:
                return generate_response(status.HTTP_400_BAD_REQUEST, 'Bad Request', str(e))
            return generate_response(status.HTTP_201_CREATED, "Medication successfully added", serializer.data)
        return generate_response(status.HTTP_400_BAD_REQUEST, "Bad Request", serializer.errors)


class LoadDroneView(APIView):
    def post(self, request):
        drone_serial_number = request.data.get('serial_number')
        medication_ids = request.data.get('medication_ids', [])
        total_weight = sum(Medication.objects.filter(id__in=medication_ids).values_list('weight', flat=True))
        try:
            drone = Drone.objects.get(serial_number=drone_serial_number)
        except Drone.DoesNotExist:
            return generate_response(status.HTTP_404_NOT_FOUND, "Drone not found.", [])

        if drone.battery_capacity < 25:
            return generate_response(status.HTTP_403_FORBIDDEN, "Drone battery level is below 25%. Cannot load.", [])

        if total_weight > drone.weight_limit:
            return generate_response(status.HTTP_403_FORBIDDEN, "Total weight exceeds drone's weight limit.", [])

        for medication_id in medication_ids:
            drone.medication.add(medication_id)

        return generate_response(status.HTTP_200_OK, "Drone loaded with medication items.", [])


class GetMedicationView(APIView):
    def get(self, request):
        medication = Medication.objects.all()
        serializer = MedicationSerializer(medication, many=True)

        return generate_response(status.HTTP_200_OK, "All Medication Fetched", serializer.data)


class GetLoadedMedicationView(APIView):
    def get(self, request, drone_serial_number):
        try:
            drone = Drone.objects.filter(serial_number=drone_serial_number)
        except Drone.DoesNotExist:
            return generate_response(status.HTTP_404_NOT_FOUND, "Drone not found.", [])

        serializer = DroneLoadedSerializer(drone, many=True)

        return generate_response(status.HTTP_200_OK, "Loaded Medication Fetched", serializer.data)


class GetAvailableDronesView(APIView):
    def get(self, request):
        available_drones = Drone.objects.filter(state__in=['IDLE', 'RETURNING'])

        if available_drones:
            data = [{'serial_number': drone.serial_number, 'model': drone.model} for drone in available_drones]
            return generate_response(status.HTTP_200_OK, "Available Drones Fetched", data)
        else:
            return generate_response(status.HTTP_204_NO_CONTENT, "No data", [])


class GetBatteryLevelView(APIView):
    def get(self, request, drone_serial_number):
        try:
            drone = Drone.objects.get(serial_number=drone_serial_number)
        except Drone.DoesNotExist:
            return generate_response(status.HTTP_404_NOT_FOUND, "Drone not found.", [])

        battery_level = drone.battery_capacity

        return generate_response(status_code=status.HTTP_200_OK, message='Success',
                                 data={"battery_level": battery_level})
