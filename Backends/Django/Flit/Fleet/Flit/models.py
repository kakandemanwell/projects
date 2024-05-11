from django.db import models

# Create your models here.

service_choices = ((1, 'oil change'), (2, 'Tire rotation'),
                   (3, 'brake replacement'))

class Vehicle(models.Model):

    type = [('SEDAN', 'Sedan'),('SUV', 'SUV'), ('TRUCK', 'Truck'), ('Trailer'),
            ('BUS', 'Bus'), ('CONVERTIBLE', 'Convertible'), ('AIRCRAFT', 'Aircraft'), ('Carriage'),
            ('VAN', 'Van'), ('TAXI', 'Taxi'), ('MOTORHOME', 'Motorhome'), ('WAGON', 'Wagon'),
            ('TRACTOR', 'Tractor'), ('BULLDOZER', 'Bulldozer'), ('AMBULANCE', 'Ambulance'), ('COUPE', 'Coupe'), ('BICYCLE', 'Bicycle'), ('CAMION/Lorry', 'Camion/Lorry')
            ]
    Vehicle_id = models.CharField(max_length=50)
    VIN = models.IntegerField()
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    Engine_size = models.IntegerField()
    Engine_type = models.CharField(max_length=20)
    Engine_model = models.CharField(max_length=20)
    Fuel_Type = models.CharField(max_length=20)
    Transmision = models.CharField(max_length=50)
    Mileage = models.DecimalField(max_digits=10, decimal_places=2)
    Licence_Plate_Number = models.CharField(max_length=10)
    last_safety_inspection_date = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=20)
    Purchase_Date = models.DateField()
    Purchase_price = models.IntegerField()
    warranty = models.IntegerField()
    location = models.CharField(max_length=200)
    STATUS_CHOICES = [
        ('IN_USE', 'In Use'),
        ('AVAILABLE', 'Available'),
        ('MAINTENANCE', 'Under Maintencnce'),
    ]

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="AVAILABLE")
    Designed_fuel_efficiency = models.DecimalField(max_digits=10, decimal_places=3)
    fuel_consumption = models.DecimalField(max_digits=10, decimal_places=4)

    last_service_date = models.DateField()
    next_service_mileage = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model} {self.Engine_size} {self.Fuel_Type} {self.Mileage}"
    def get_description(self):
        return f"{self.year} {self.make} {self.model}"
    
    def get_specifications(self):
        return f"{self.year} {self.make} {self.model}, {self.Engine_size} {self.Engine_model} {self.Engine_type} {self.Fuel_Type} {self.Mileage}"

    def is_service_due(self):
        """Returns True if the mileage exceeds next service mileage."""
        return self.Mileage >= self.next_service_mileage
    
    def schedule_maintenance(self, miles_until_service):
        """Schedules the next maintenance after a given mileage."""
        self.next_service_mileage = self.mileage + miles_until_service
 
    def calculate_fuel_efficiency(self):
        """Calculate fuel efficiency in miles per gallon (MPG).
         This can help track fuel costs and vehicle efficiency over time.
        """
        if self.fuel_consumption > 0:
            return self.fuel_consumption / self.fuel_consumption
        return None
    
    def get_status(self):
        return self.status
    
    def total_mileage(self):
        return self.Mileage


class Maintenance(models.Model):
    Service_Date = models.DateField()
    Service_Type = models.CharField(max_length=200)
    Service_provider = models.CharField(max_length=100)
    Notes = models.TextField()


class Driver(models.Model):
    """Defines a Driver in the system.
    Args;
        first_name: (str) - "John"
        last_name(str): "Smith"
        Driving_licence_id(integer): 01234567899876
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    Driving_licence_id = models.CharField(max_length=15)
    license_expiry_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.Driving_licence_id}"