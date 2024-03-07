import folium
from .models import Crag, Site
from folium.plugins import MarkerCluster
from django.template.loader import  render_to_string
from .filters import CragFilter
from .forms import CragNameFilterForm, AddSite
from django.shortcuts import get_object_or_404, render
from .utils import crag_items, marker_color_rodzaj, feature_group_rodzaj, marker_color_skala, feature_group_skala
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):

    #create map object
    m = folium.Map(location = [51.8948, 19.6385],min_zoom =6, zoom_start=3, width = '100%', height = '70%', max_bounds=True)
    folium.plugins.Geocoder(add_marker=False, position="bottomright").add_to(m)
    folium.plugins.Fullscreen(position="topright", title="pełny ekran", title_cancel="zamknij pełny ekran", force_separate_button=True).add_to(m)
    #store  feature groups

    feature_bulder = folium.FeatureGroup(name='Buldery')
    feature_drogi = folium.FeatureGroup(name='Wspinanie sportowe')
    feature_trad = folium.FeatureGroup(name='Trad')
    feature_scianka = folium.FeatureGroup(name='Scianka')
    # marker_cluster = MarkerCluster().add_to(m)

    crags = Crag.objects.all()
    for item in crags:

        lat, lon, name, rodzaj, opis, wyceny, skala, strony_linki, filmy_linki, topo, google_maps = crag_items(item)

        popup_data = {'name':name, 'rodzaj':rodzaj,'opis':opis, 'wyceny':wyceny, 'skala':skala,
                      'sites':strony_linki, 'movies':filmy_linki, 'google_maps':google_maps, 'topos':topo}

        #here we edit popups
        popup_text = render_to_string('popups/popup1.html', popup_data)

        #here we make markers

        marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color=marker_color_rodzaj(rodzaj), prefix = 'fa', icon='chain'),tooltip=name)
        feature_group_rodzaj(marker,rodzaj,feature_bulder,feature_drogi,feature_trad, feature_scianka)

    feature_bulder.add_to(m)
    feature_drogi.add_to(m)
    feature_trad.add_to(m)
    feature_scianka.add_to(m)

    folium.LayerControl().add_to(m)
    # html_to_insert = "<style>.leaflet-popup-content-wrapper, .leaflet-popup.tip {background: linear-gradient(to bottom, #f95959 10%, #ffffff 150%) !important; }</style>"
    # m.get_root().header.add_child(folium.Element(html_to_insert))

    #html representation of map
    m = m._repr_html_()

    context = {
        'm':m,
    }

    return(render(request, 'index.html', context))

def szukaj(request):
    query_params = request.GET
    form = CragNameFilterForm(initial=query_params)
    crag_filter = CragFilter(request.GET, queryset=Crag.objects.all())

    context = {
        'form': form,
        'crags': crag_filter.qs.order_by('nazwa')
    }
    return render(request, 'szukaj.html', context)

def miejsca(request, nazwa):
    crag = get_object_or_404(Crag, nazwa=nazwa)
    site = Site.objects.all()
    context = {
        'crag':crag,
        'site':site
    }
    return render(request, 'miejsca.html', context)

def dodaj(request):

    return render(request, 'dodaj/dodaj_base.html')

def dodaj_site(request):

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AddSite(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            messages.add_message(request, messages.INFO, "Dodane")
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/site/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddSite()

    return render(request, 'dodaj/dodaj_site.html', {"form": form})

def dodaj_movie(request):

    return render(request, 'dodaj/dodaj_movie.html')

def info(request):

    return render(request, 'info.html')

def mapa_skaly(request):
    #create map object
    m = folium.Map(location = [51.8948, 19.6385],min_zoom =6, zoom_start=3, width = '100%', height = '70%', max_bounds=True)
    folium.plugins.Geocoder(add_marker=False, position="bottomright").add_to(m)
    folium.plugins.Fullscreen(position="topright", title="pełny ekran", title_cancel="zamknij pełny ekran", force_separate_button=True).add_to(m)
    #store  feature groups

    feature_wapien = folium.FeatureGroup(name='Wapień')
    feature_piaskowiec = folium.FeatureGroup(name='Piaskowiec')
    feature_granit = folium.FeatureGroup(name='Granit')
    feature_bazalt = folium.FeatureGroup(name='Bazalt')
    feature_gnejs = folium.FeatureGroup(name='Gnejs')
    feature_beton = folium.FeatureGroup(name='Beton')
    feature_plastik = folium.FeatureGroup(name='Plastik')
    # marker_cluster = MarkerCluster().add_to(m)

    crags = Crag.objects.all()
    for item in crags:

        lat, lon, name, rodzaj, opis, wyceny, skala, strony_linki, filmy_linki, topo, google_maps = crag_items(item)

        popup_data = {'name':name, 'rodzaj':rodzaj,'opis':opis, 'wyceny':wyceny, 'skala':skala,
                      'sites':strony_linki, 'movies':filmy_linki, 'google_maps':google_maps, 'topos':topo}

        #here we edit popups
        popup_text = render_to_string('popups/popup1.html', popup_data)

        #here we make markers
        #
        marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color=marker_color_skala(skala), prefix = 'fa', icon='hammer'),tooltip=name)

        if skala == Crag.Piaskowiec:
            marker.add_to(feature_piaskowiec)
        elif skala == Crag.Wapien:
            marker.add_to(feature_wapien)
        elif skala == Crag.Granit:
            marker.add_to(feature_granit)
        elif skala == Crag.Plastik:
            marker.add_to(feature_plastik)
        elif skala == Crag.Beton:
            marker.add_to(feature_beton)
        elif skala == Crag.Gnejs:
            marker.add_to(feature_gnejs)
        elif skala == Crag.Bazalt:
            marker.add_to(feature_bazalt)
        #feature_group_skala(marker,rodzaj,feature_wapien,feature_piaskowiec,feature_granit, feature_plastik,feature_gnejs,feature_beton, feature_bazalt)

    feature_wapien.add_to(m)
    feature_piaskowiec.add_to(m)
    feature_granit.add_to(m)
    feature_plastik.add_to(m)
    feature_beton.add_to(m)
    feature_bazalt.add_to(m)
    feature_gnejs.add_to(m)

    folium.LayerControl().add_to(m)
    #html representation of map
    m = m._repr_html_()

    context = {
        'm':m,
    }

    return(render(request, 'mapy/mapa_skaly.html', context))

def mapa_wyceny(request):
    #create map object
    m = folium.Map(location = [51.8948, 19.6385],min_zoom =6, zoom_start=3, width = '100%', height = '70%', max_bounds=True)
    folium.plugins.Geocoder(add_marker=False, position="bottomright").add_to(m)
    folium.plugins.Fullscreen(position="topright", title="pełny ekran", title_cancel="zamknij pełny ekran", force_separate_button=True).add_to(m)
    #store  feature groups

    feature_bulder = folium.FeatureGroup(name='Buldery')
    feature_drogi = folium.FeatureGroup(name='Wspinanie sportowe')
    feature_trad = folium.FeatureGroup(name='Trad')
    feature_scianka = folium.FeatureGroup(name='Scianka')
    # marker_cluster = MarkerCluster().add_to(m)

    crags = Crag.objects.all()
    for item in crags:

        lat, lon, name, rodzaj, opis, wyceny, skala, strony_linki, filmy_linki, topo, google_maps = crag_items(item)

        popup_data = {'name':name, 'rodzaj':rodzaj,'opis':opis, 'wyceny':wyceny, 'skala':skala,
                      'sites':strony_linki, 'movies':filmy_linki, 'google_maps':google_maps, 'topos':topo}

        #here we edit popups
        popup_text = render_to_string('popups/popup1.html', popup_data)

        #here we make markers

        marker = folium.Marker([lon, lat], popup=popup_text, icon=folium.Icon(color=marker_colour(rodzaj), prefix = 'fa', icon='chain'),tooltip=name)
        feature_group(marker,rodzaj,feature_bulder,feature_drogi,feature_trad, feature_scianka)

    feature_bulder.add_to(m)
    feature_drogi.add_to(m)
    feature_trad.add_to(m)
    feature_scianka.add_to(m)

    folium.LayerControl().add_to(m)
    #html representation of map
    m = m._repr_html_()

    context = {
        'm':m,
    }

    return(render(request, 'mapy/mapa_wyceny.html', context))
