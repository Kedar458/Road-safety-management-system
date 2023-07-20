from django.db import models
from django.contrib.auth.models import User


class city(models.Model):
    name=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    pincode=models.PositiveIntegerField()    

    def __str__(self):
        return self.name

class area(models.Model):
    name=models.CharField(max_length=255)
    city_id=models.ForeignKey(city,on_delete=models.CASCADE)
    pincode=models.PositiveIntegerField()    

    def __str__(self):
       return self.name

street_type=[('One Way','One Way'),('Two Way','Two Way')]

class road(models.Model):
    name=models.CharField(max_length=255)
    area_id=models.ForeignKey(area,on_delete=models.CASCADE)
    length=models.DecimalField(decimal_places=2, default=0, max_digits=10)
    lanes=models.PositiveIntegerField()
    speed_limit=models.PositiveIntegerField()
    street_type=models.CharField(max_length=255,choices=street_type)
    def __str__(self):
       return self.name

age_group=[('0-10','0-10'),('11-20','11-20'),('21-30','21-30'),('31-40','31-40'),('40-60','40-60'),
('60+','60+')]
accident_type=[('Rear-end collision','Rear-end collision'),('Side-impact collision','Side-impact collision'),
('Rollover','Rollover'),('Head on collisions','Head on collisions')]
class accidents(models.Model):
    road_id=models.ForeignKey(area,on_delete=models.CASCADE)
    year= models.CharField(max_length=255)
    accident_type=models.CharField(max_length=255,choices=accident_type)
    age_group=models.CharField(max_length=255,choices= age_group)
    Number_of_Accidents=models.CharField(max_length=255)

    
 
vehicle_type=[('bike','bike'),('car','car'),('truck','truck'),('bus','bus')]
class accidents_reported(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    area_id=models.ForeignKey(area,on_delete=models.CASCADE)
    accident_type=models.CharField(max_length=255,choices= accident_type)
    death_rate=models.PositiveIntegerField()
  

class complaint(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    city_id=models.ForeignKey(city,on_delete=models.CASCADE)
    area_id=models.ForeignKey(area,on_delete=models.CASCADE)
    description=models.CharField(max_length=255)





