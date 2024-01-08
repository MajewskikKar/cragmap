from django.shortcuts import render
import folium
from .models import Crag
from folium.plugins import MarkerCluster
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
import branca
#main site
def index(request):
    popup_template = get_template('popups/popup1.html')

    #create map object
    m = folium.Map(location = [51.8948, 19.6385],min_zoom =6, zoom_start=3)


    #store  feature groups

    feature_bulder= folium.FeatureGroup(name='Buldery')
    feature_drogi = folium.FeatureGroup(name='Wspinanie sportowe')
    feature_trad = folium.FeatureGroup(name='Trad')


    #marker cluster


    #marker_cluster = MarkerCluster().add_to(m)

    crags = Crag.objects.all()
    for item in crags:

        #here we store values
        lat = item.latitude
        lon = item.longitude
        name = item.nazwa
        bulder = item.bulder
        opis = item.opis
        wyceny = item.wyceny
        skala = item.skala
        strony_linki = item.site_set.all() #from related table Site
        filmy_linki = item.movie_set.all()
        popup_data = {'name':name, 'bulder':bulder,'opis':opis, 'wyceny':wyceny, 'skala':skala,
                      'sites':strony_linki, 'movies':filmy_linki}
        #here we edit popups
        popup_text = render_to_string('popups/popup1.html', popup_data)
        #here we make markers
        if bulder == '0': #marker for climbing routes
            marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color="green", prefix = 'fa', icon='chain'),
                                   tooltip=name)
            marker.add_to(feature_drogi)
        elif bulder == '1': #marker for boulders
            marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color="red", prefix = 'fa', icon='chain'),
                                   tooltip=name)
            marker.add_to(feature_bulder)
        elif bulder =='2': #marker for trad
            marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color="orange", prefix = 'fa', icon='chain'),
                                   tooltip=name)
            marker.add_to(feature_trad)

    feature_bulder.add_to(m)
    feature_drogi.add_to(m)
    feature_trad.add_to(m)

    folium.LayerControl().add_to(m)


    #html representation of map
    m = m._repr_html_()

    context = {
        'm':m,
    }

    return(render(request, 'index.html', context))

def szukaj(request):
    return HttpResponse("Szukajka")
