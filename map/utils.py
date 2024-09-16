from .models import Crag

def crag_items(item):

        lat = item.latitude
        lon = item.longitude
        wysokosc = item.wysokosc
        name = item.nazwa
        rodzaj = item.rodzaj
        opis = item.opis
        wyceny = item.wyceny
        skala = item.skala
        ilosc_drog = item.ilosc_drog
        wiek_skal = item.wiek_skal
        strony_linki = item.site_set.all()
        filmy_linki = item.movie_set.all()
        topo = item.topo_set.all()
        google_maps = f'https://maps.google.com/?q={lon},{lat}'
        return lat, lon, name, rodzaj, opis, wyceny, skala, strony_linki, filmy_linki, topo, google_maps, ilosc_drog, wiek_skal, wysokosc



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
                return "lightred"
        elif skala == Crag.Plastik:
                return "darkblue"
        elif skala == Crag.Beton:
                return "gray"
        elif skala == Crag.Gnejs:
                return "darkred"
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


def feature_group_wyceny(marker, wyceny, feature_latwe, feature_srednie, feature_trudne, feature_zroznicowane):

        if wyceny == Crag.Latwe:
                marker.add_to(feature_latwe)
        elif wyceny == Crag.Srednie:
                marker.add_to(feature_srednie)
        elif wyceny == Crag.Trudne:
                marker.add_to(feature_trudne)
        elif wyceny == Crag.Zroznicowane:
                marker.add_to(feature_zroznicowane)

def marker_color_icon(wyceny):

        if wyceny == Crag.Latwe:
                return 'baby-carriage'
        elif wyceny == Crag.Srednie:
                return 'user-graduate'
        elif wyceny == Crag.Trudne:
                return 'star'
        elif wyceny == Crag.Zroznicowane:
                return 'users'
def html_background_color(rodzaj):
        if rodzaj == Crag.Sport:
                return "{background: linear-gradient(to bottom, #dfdfdf 10%, #ffffff 150%) !important; }"
        else:
                return "{background: linear-gradient(to bottom, #f95959 10%, #ffffff 150%) !important; }"

def marker_icon(ilosc_drog):
        if ilosc_drog == Crag.Mala:
                return 's'
        elif ilosc_drog == Crag.Srednia:
                return 'm'
        elif ilosc_drog == Crag.Duza:
                return 'l'
