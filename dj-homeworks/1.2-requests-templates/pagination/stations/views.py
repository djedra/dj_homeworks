import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    return redirect(reverse('bus_stations'))




def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_number = int(request.GET.get('page', 1))
    station_list = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            station_list.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})

    paginator = Paginator(station_list, 10)
    page = paginator.get_page(page_number)


    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)