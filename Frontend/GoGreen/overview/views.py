from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .generate_visuals import get_plots


@login_required(login_url='login-index')
def index(request):
    get_plots() # Calling the get_plots function from generate_visuals to refresh the data in the graphs
    return render(request, 'overview/index.html')
