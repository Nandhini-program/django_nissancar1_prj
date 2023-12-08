from django.db import models


# Create your models here.
class client(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number= models.IntegerField()
    date_of_birth = models.DateField()
    current_datetime = models.DateTimeField(null=True)  # Automatically set when the object is created
    # update_datetime = models.DateTimeField(auto_now=True)  # Automatically set whenever the object is updated
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.firstname}{self.lastname}"

class client_car(models.Model):
    client_id=models.IntegerField()
    modelname = models.CharField(max_length=50)
    modelno = models.CharField(max_length=100)
    Price = models.FloatField()
    fueltype = models.CharField(max_length=50)
    transmission = models.CharField(max_length=100)
    engine_size= models.CharField(max_length=100)
    Mileage = models.CharField(max_length=50)
    Warranty = models.CharField(max_length=100)
    seating_capacity= models.CharField(max_length=20)
    size = models.CharField(max_length=100)
    fueltank = models.CharField(max_length=50)
    subject=models.TextField()

    def __str__(self):
        return f"{self.modelname}{self.modelno}"
    

