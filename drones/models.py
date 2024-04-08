from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.utils import timezone

from django.db import models

class Drone(models.Model):
    STATE_CHOICES = [
        ('IDLE', 'IDLE'),
        ('LOADING', 'LOADING'),
        ('LOADED', 'LOADED'),
        ('DELIVERING', 'DELIVERING'),
        ('DELIVERED', 'DELIVERED'),
        ('RETURNING', 'RETURNING'),
    ]

    MODEL_CHOICES = [
        ('Lightweight', 'Lightweight'),
        ('Middleweight', 'Middleweight'),
        ('Cruiserweight', 'Cruiserweight'),
        ('Heavyweight', 'Heavyweight'),
    ]

    serial_number = models.CharField(max_length=100, unique=True, null=False)
    model = models.CharField(max_length=20, choices=MODEL_CHOICES)
    weight_limit = models.FloatField(validators=[MaxValueValidator(500)]) 
    battery_capacity = models.FloatField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)])
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    medication = models.ManyToManyField('Medication', blank=True,related_name="medication")

    def __str__(self):
        return f"Drone {self.serial_number} - {self.model}"

class Medication(models.Model):
    name_validator = RegexValidator(
        r'^[A-Za-z0-9\-\' ]+$',
        'Only letters, numbers, hyphen, and apostrophe are allowed in the name.'
    )
    code_validator = RegexValidator(
        r'^[A-Z0-9_]+$',
        'Only uppercase letters, numbers, and underscore are allowed in the code.'
    )

    name = models.CharField(max_length=100,unique=True, validators=[name_validator])
    weight = models.FloatField(validators=[MinValueValidator(0)])
    code = models.CharField( max_length=100, unique=True,validators=[code_validator])
    image = models.ImageField(upload_to='uploads/')


    def __str__(self):
        return self.name

class BatteryAuditLog(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    battery_level = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.drone.serial_number} - Battery Level: {self.battery_level}%"