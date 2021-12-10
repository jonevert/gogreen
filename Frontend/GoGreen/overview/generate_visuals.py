from pathlib import Path
import numpy as np
import plotly.express as px
from CarList.models import instances, cars
from django.db.models import *

plot_folder = Path("GoGreen/templates/overview/plots/")



# Update axes and buttons for the figures
def update_fig(fig):
    fig.update_layout(font_size=12)
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )


# Creates a plot showing the total number of instances for any given date
def no_cars(dates, no_instances):

    df = {'Date': dates, 'Count': no_instances}
    fig = px.line(df, x='Date', y='Count')
    update_fig(fig)
    file_name = plot_folder / "car_count.html"
    fig.write_html(file_name, full_html=False, include_plotlyjs="cdn")

# Creates a plot showing the average emission value over all instances for any given date
def avg_emissions(dates):

    emissions = []
    for d in dates:
        p = instances.objects.filter(timestamp__date=d).values_list('plate_nr', flat=True)
        emissions.append(
            np.average(cars.objects.filter(plate_nr__in=p).values_list('co2', flat=True))
        )

    df = {'Date': dates, 'CO2 [g/km]': emissions}

    fig = px.line(df, x='Date', y='CO2 [g/km]')

    update_fig(fig)

    file_name = plot_folder / "avg_emissions.html"
    fig.write_html(file_name, full_html=False, include_plotlyjs="cdn")


# Creates a plot showing the percentage of instances where the cars have zero emissions for any given date
def zero_ratio(dates, no_instances):

    no_zeros = []
    for d in dates:
        p = instances.objects.filter(timestamp__date=d).values_list('plate_nr', flat=True)
        no_zeros.append(
            cars.objects.filter(plate_nr__in=p, co2=0).count()
        )

    ratio = [(i / j)*100 for i, j in zip(no_zeros, no_instances)]

    df = {'Date': dates, 'Zero Emission [%]': ratio}

    fig = px.line(df, x='Date', y='Zero Emission [%]')

    update_fig(fig)

    file_name = plot_folder / "zero_ratio.html"
    fig.write_html(file_name, full_html=False, include_plotlyjs="cdn")


# Generate all plots
# All plots are generated as individual html files that are then included in the overview page
def get_plots():
    dates = instances.objects.dates('timestamp', 'day')
    no_instances = instances.objects.dates('timestamp', 'day').values_list(Count('pk'), flat=True)
    no_cars(dates, no_instances)
    avg_emissions(dates)
    zero_ratio(dates, no_instances)

