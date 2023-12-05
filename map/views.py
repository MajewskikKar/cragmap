from django.shortcuts import render
import folium
from .models import Crag
# Create your views here.

def index(request):

    #create map object
    m = folium.Map(location = [51.8948, 19.6385],min_zoom =6, zoom_start=2)
    crags = Crag.objects.all()

    #
    for item in crags:

        #here we store values
        lat = item.latitude
        lon = item.longitude
        name = item.nazwa
        buld = item.bulder
        strony_linki = item.site_set.all()

        #here we edit popups
        popup_text = f'''{name}
'''
        for site in strony_linki:
                popup_text += f'<a href="{site.link}" target ="_blank">{site.nazwa_strony}</a><br>'

        #here we make markers
        if buld == '0': #marker for climbing routes
            folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color="green", prefix = 'fa', icon='chain')).add_to(m)
        elif buld == '1': #marker for boulders
            folium.Marker([lon, lat], popup=name, icon=folium.Icon(color="red", prefix = 'fa', icon='chain')).add_to(m)
        elif buld =='2': #marker for others?
            folium.Marker([lon, lat], popup=name, icon=folium.Icon(color="yellow", prefix = 'fa', icon='chain')).add_to(m)

    #html representation of map
    m = m._repr_html_()

    context = {
        'm':m,
    }

    return(render(request, 'index.html', context))
