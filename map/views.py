from django.shortcuts import render
import folium
from .models import Crag
from folium.plugins import MarkerCluster
from django.template.loader import get_template, render_to_string
from .filters import CragFilter
#main site
def index(request):
    popup_template = get_template('popups/popup1.html')

    #create map object
    m = folium.Map(location = [51.8948, 19.6385],min_zoom =6, zoom_start=3, width = '100%', height = '67%', max_bounds=True)
    folium.plugins.Geocoder(add_marker=False, position="bottomright").add_to(m)
    folium.plugins.Fullscreen(position="topright", title="pełny ekran", title_cancel="zamknij pełny ekran", force_separate_button=True).add_to(m)
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
        google_maps = f'https://maps.google.com/?q={lon},{lat}'
        pogoda = f'https://openweathermap.org/weathermap?basemap=map&cities=false&layer=temperature&lat={{lat}}&lon={{lon}}&zoom=10'

        popup_data = {'name':name, 'bulder':bulder,'opis':opis, 'wyceny':wyceny, 'skala':skala,
                      'sites':strony_linki, 'movies':filmy_linki, 'google_maps':google_maps}

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
    crag_filter = CragFilter(request.GET, queryset=Crag.objects.all())
    context = {
        'form': crag_filter.form,
        'crags': crag_filter.qs
    }
    return render(request, 'szukaj.html', context)
