import json

from django.db.models.query_utils import select_related_descend
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import instances, location, cars


@login_required(login_url='login-index')
def index(request):
    instance = instances.objects.order_by("-id")[0]             # Get the most recent instance
    list_recent = instances.objects.order_by("-id")[:20]        # Get a set of 20 most recent instances
    loc = location.objects.get(pk=instance.location_id)         # Get the location of the most recent instance
    car = cars.objects.filter(plate_nr=instance.plate_nr).get() # Get the car information of the most recent instance

    return render(request, 'CarList/index.html',
                  {'Instance': instance, 'PlateList': list_recent, 'Location': loc, 'Car': car})


# This is executed when the user selects a licenence plate from the list in the Activity tab
@login_required(login_url='login-index')
def instance_info(request, instance_pk):
    instance = instances.objects.filter(pk=instance_pk).get()   # Get the instance specified in the request
    loc = location.objects.get(pk=instance.location_id)         # Get location of that instance
    list_recent = instances.objects.order_by("-id")[:20]        # Get a set of 20 most recent instances
    car = cars.objects.filter(plate_nr=instance.plate_nr).get() # Get the car information of the requested instance
    return render(request, 'CarList/index.html',
                  {'Instance': instance, 'PlateList': list_recent, 'Location': loc, 'Car': car})

