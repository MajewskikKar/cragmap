from django.shortcuts import render
import folium
from .models import Crag
from folium.plugins import MarkerCluster
from django.http import HttpResponse
import os
from django.template.loader import get_template, render_to_string
from templates import popups
# Create your views here.
# test

def index(request):
    popup_template = get_template('popups/popup1.html')
    #create map object
    m = folium.Map(location = [51.8948, 19.6385],min_zoom =6, zoom_start=3)
    crags = Crag.objects.all()

    #store  feature groups
    feature_bulder= folium.FeatureGroup(name='Buldery',show=True)
    feature_drogi = folium.FeatureGroup(name='Drogi ubezpieczone')


    #marker cluster
    marker_cluster = MarkerCluster().add_to(m)
    for item in crags:

        #here we store values
        lat = item.latitude
        lon = item.longitude
        name = item.nazwa
        buld = item.bulder
        strony_linki = item.site_set.all() #from related table Site

        #here we edit popups
        popup_text = render_to_string('popups/popup1.html', {'name': name, 'lat':lat})

        #here we make markers
        if buld == '0': #marker for climbing routes
            marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color="green", prefix = 'fa', icon='chain'),
                                   tooltip=name)
            marker.add_to(marker_cluster)
        elif buld == '1': #marker for boulders
            marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color="red", prefix = 'fa', icon='chain'),
                                   tooltip=name)
            marker.add_to(marker_cluster)
        elif buld =='2': #marker for others?
            marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color="yellow", prefix = 'fa', icon='chain'),
                                   tooltip=name)
            marker.add_to(marker_cluster)

    feature_bulder.add_to(marker_cluster)
    feature_drogi.add_to(marker_cluster)
    folium.LayerControl().add_to(m)
    #html representation of map
    m = m._repr_html_()

    context = {
        'm':m,
    }

    return(render(request, 'index.html', context))

def szukaj(request):
    return HttpResponse("Szukajka")
