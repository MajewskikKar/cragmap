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

def marker_color_rodzaj(rodzaj):

        if rodzaj == Crag.Sport:
                return "green"
        elif rodzaj == Crag.Bulder:
                return "red"
        elif rodzaj == Crag.Trad:
                return "orange"
        elif rodzaj == Crag.Scianka:
                return "blue"

def marker_color_skala(skala):

        if skala == Crag.Piaskowiec:
                return "red"
        elif skala == Crag.Wapien:
                return "blue"
        elif skala == Crag.Granit:
                return "pink"
        elif skala == Crag.Plastik:
                return "darkblue"
        elif skala == Crag.Beton:
                return "gray"
        elif skala == Crag.Gnejs:
                return "beige"
        elif skala == Crag.Bazalt:
                return "black"

def feature_group_rodzaj(marker, rodzaj, feature_bulder, feature_drogi, feature_trad, feature_scianka):

        if rodzaj == Crag.Sport:
            marker.add_to(feature_drogi)
        elif rodzaj == Crag.Bulder:
            marker.add_to(feature_bulder)
        elif rodzaj == Crag.Trad:
            marker.add_to(feature_trad)
        elif rodzaj == Crag.Scianka:
            marker.add_to(feature_scianka)

def feature_group_skala(marker,skala,feature_wapien,feature_piaskowiec,feature_granit, feature_plastik,feature_gnejs,feature_beton, feature_bazalt):

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

def html_background_color(rodzaj):
        if rodzaj == Crag.Sport:
                return "{background: linear-gradient(to bottom, #dfdfdf 10%, #ffffff 150%) !important; }"
        else:
                return "{background: linear-gradient(to bottom, #f95959 10%, #ffffff 150%) !important; }"

