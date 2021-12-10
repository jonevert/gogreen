from django.db import models


# class location(models.Model):
#     name = models.CharField(max_length=120)
#     region = models.CharField(max_length=120)
#     zip = models.IntegerField()
#
#     objects = models.Manager()
#
#     def __str__(self):
#         return self.name
#
#
# class cars(models.Model):
#     plate_nr = models.CharField(max_length=10)
#     make = models.CharField(max_length=120)
#     model = models.CharField(max_length=120)
#     year = models.IntegerField()
#     color = models.CharField(max_length=120)
#     #fuel_type = models.CharField(max_length=120) not available
#     co2 = models.IntegerField()
#
#     objects = models.Manager()
#
#     def __str__(self):
#         return self.plate_nr
#
#
# class instances(models.Model):
#     plate_nr = models.CharField(max_length=120)
#     location_id = models.IntegerField(models.ForeignKey(location, on_delete=models.CASCADE))
#     timestamp = models.DateTimeField(auto_now_add=True)
#     no_passangers = models.IntegerField(blank=True, null=True, default = "")
#     impath = models.CharField(max_length=255)
#     isvalid = models.BooleanField(default=True)
#
#     objects = models.Manager()
#
#     def __str__(self):
#         return "Plate: " + str(self.plate_nr)

# Create your models here.


