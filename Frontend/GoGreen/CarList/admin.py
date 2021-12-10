from django.contrib import admin
from .models import instances
from .models import cars
from .models import location

admin.site.register(instances)
admin.site.register(cars)
admin.site.register(location)
