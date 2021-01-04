from django.db import models

# Create your models here.

class Car(models.Model):
    SERVICE_CHOICE = [('P','Platinum'),('G','Gold')]
    car_model = models.CharField(max_length = 100)
    car_owner = models.CharField(max_length = 100)
    car_notes = models.CharField(max_length = 100)
    car_number = models.CharField(max_length = 30)
    description = models.TextField(max_length=1000)
    car_price = models.IntegerField(null=True)
    service_type = models.CharField(choices = SERVICE_CHOICE,max_length = 1,blank = True)
    submission_data = models.DateField()
    year_old = models.IntegerField(null=True)
    servicing = models.ManyToManyField('Service',blank = True)
    category = models.CharField(max_length=50, default="")
    Images = models.ImageField(upload_to = 'photos')
    def __str__(self):
        return self.car_model
    
class Service(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    

    
    