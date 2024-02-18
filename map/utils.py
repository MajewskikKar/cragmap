from .models import Crag

def crag_items(item):

        lat = item.latitude
        lon = item.longitude
        name = item.nazwa
        rodzaj = item.rodzaj
        opis = item.opis
        wyceny = item.wyceny
        skala = item.skala
        strony_linki = item.site_set.all()
        filmy_linki = item.movie_set.all()
        topo = item.topo_set.all()
        google_maps = f'https://maps.google.com/?q={lon},{lat}'
        return lat, lon, name, rodzaj, opis, wyceny, skala, strony_linki, filmy_linki, topo, google_maps

def marker_colour(rodzaj):
        if rodzaj == Crag.Sport:
                return "green"
        elif rodzaj == Crag.Bulder:
                return "red"
        elif rodzaj == Crag.Trad:
                return "orange"
        elif rodzaj == Crag.Scianka:
                return "blue"

def feature_group(marker, rodzaj, feature_bulder, feature_drogi, feature_trad, feature_scianka):
    if rodzaj == Crag.Sport:
            marker.add_to(feature_drogi)
    elif rodzaj == Crag.Bulder:
            marker.add_to(feature_bulder)
    elif rodzaj == Crag.Trad:
            marker.add_to(feature_trad)
    elif rodzaj == Crag.Scianka:
            marker.add_to(feature_scianka)

def html_background_color(rodzaj):
        if rodzaj == Crag.Sport:
                return "{background: linear-gradient(to bottom, #dfdfdf 10%, #ffffff 150%) !important; }"
        else:
                return "{background: linear-gradient(to bottom, #f95959 10%, #ffffff 150%) !important; }"

