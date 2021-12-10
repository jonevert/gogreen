from django.db import models

#file models.py should be in main app folder



class location(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    zip = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "location"


class cars(models.Model):
    objects = models.Manager()
    plate_nr = models.CharField(max_length=10)
    make = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    year = models.IntegerField()
    color = models.CharField(max_length=120)
    #fuel_type = models.CharField(max_length=120) not available
    co2 = models.IntegerField()

    def __str__(self):
        return self.plate_nr

    class Meta:
        db_table = "cars"

class instances(models.Model):
    objects = models.Manager()
    plate_nr = models.CharField(max_length=120)
    location_id = models.IntegerField(models.ForeignKey(location, on_delete=models.CASCADE))
    timestamp = models.DateTimeField(auto_now_add=True)
    no_passangers = models.IntegerField(blank=True, null=True, default = "")
    impath = models.CharField(max_length=255)
    isvalid = models.BooleanField(default=True)

    def __str__(self):
        return "Plate: " + str(self.plate_nr)

    #to override table name
    class Meta:
        db_table = "instances"


#tafla sem geymir allt fra samgongustofu
class samgongustofa(models.Model):
    permno = models.CharField(max_length=50, blank=True, null=True)
    regno = models.CharField(max_length=50, blank=True, null=True)
    vin = models.CharField(max_length=50, blank=True, null=True)
    make = models.CharField(max_length=120, blank=True, null=True)
    model = models.CharField(max_length=120, blank=True, null=True)
    color = models.CharField(max_length=120, blank=True, null=True)
    # timestamp = registration date - postgres vildi ekki leyfa mér
    # að kalla þetta neitt annað
    timestamp = models.DateTimeField(blank=True, null=True)
    vehicleStatus = models.CharField(max_length=120, blank=True, null=True)
    nextVehicleMainInspection = models.DateField(blank=True, null=True)
    co2 = models.IntegerField(blank=True, null=True)
    weightedCo2 = models.IntegerField(blank=True, null=True)
    co2WLTP = models.IntegerField(blank=True, null=True)
    weightedCo2WLTP = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    massLaden = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "samgongustofa"
