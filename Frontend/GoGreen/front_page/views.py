import datetime

import numpy as np
from CarList.models import instances, cars, location
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ImprovedUserCreationForm

# When the front page is loaded, this returns information for the daily summary,
# as well as the information on the most recent instance
@login_required(login_url='login-index')
def index(request):
    newest_car = instances.objects.order_by("-id")[0]
    inst_today = instances.objects.filter(timestamp__date=datetime.date.today())
    cars_today = cars.objects.filter(plate_nr__in=inst_today.values_list('plate_nr', flat=True))

    # If there are instances registerd for this day, data is set and percentages calculated
    if inst_today.count() > 0:
        no_zeros = cars_today.filter(co2=0).count()
        no_cars = cars_today.count()
        ratio = (no_zeros / no_cars) * 100
        data = {
            'Avg_CO2': np.average(cars_today.values_list('co2', flat=True)),
            'no_total': no_cars,
            'no_zeros': no_zeros,
            'Ratio': ratio,
            'Date': datetime.date.today()
        }
    # If there are no instances, the data has to be implemented differently
    # as it would otherwise cause errors, f.x. by dividing with 0
    else:
        data = {
            'Avg_CO2': 0,
            'no_total': 0,
            'no_zeros': 0,
            'Ratio': -1,
            'Date': datetime.date.today()
        }

    loc = location.objects.filter(pk=newest_car.location_id).get()

    return render(request, 'front_page/index.html', {
        'latest': {
            'car_info': cars.objects.filter(plate_nr=newest_car.plate_nr).get(),
            'inst_info': newest_car,
            'loc': loc},
        'Instances': inst_today,
        'Cars': cars_today,
        'Data': data
    })


# Post view for registration to the site
def register(request):
    if request.method == 'POST':
        form = ImprovedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created, please log in.')
            return redirect('login-index')
    else:
        form = ImprovedUserCreationForm()
    return render(request, 'front_page/register.html', {'form': form})


# Return the 'About us' page
def about(request):
    return render(request, 'front_page/about_us.html')

# Return the 'Documentation' page
def docs(request):
    return render(request, 'front_page/documentation.html')
