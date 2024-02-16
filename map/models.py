from django.db import models


#klasa Crag jest główną, obsługującą punkty na mapie. Pozostałe klasy są relacyjne dla Crag.
class Crag(models.Model):

    #rodzaj miejsca
    Bulder = "Bulder"
    Sport = "Sport"
    Trad = "Trad"
    Scianka = "Scianka"
    Inne = "Inne"
    Bd = "Brak danych"

    #ilosc dróg
    Mala = "<25"
    Srednia = "25-100"
    Duza = ">100"

    #wyceny
    Latwe = "Łatwe"
    Srednie = "Średnie"
    Trudne = "Trudne"
    Zroznicowane = "Zróżnicowane"

    #skaly
    Piaskowiec = "Piaskowiec"
    Wapien = "Wapień"
    Granit = "Granit"
    Bazalt = "Bazalt"
    Plastik = "Plastik"
    Beton = "Beton"



    rodzaj_choices =[
        (Bulder, "bulder"),
        (Sport, "drogi ubezpieczone"),
        (Trad, "własna asekuracja"),
        (Scianka, "ścianka wspinaczkowa"),
        (Bd, "brak danych")
    ]

    ilosc_drog_choices = [
        (Bd,'brak danych'),
        (Mala,'<25'),
        (Srednia,'25-100'),
        (Duza,'>100')
    ]

    wyceny_choices = [
        (Bd,'brak danych'),
        (Latwe, 'łatwe'),
        (Srednie, 'średnie'),
        (Trudne, 'trudne'),
        (Zroznicowane, 'zróżnicowane')
    ]

    skala_choices = [(Wapien, 'wapień'),
                     (Piaskowiec, 'piaskowiec'),
                     (Granit, 'granit'),
                     (Bazalt, 'bazalt'),
                     (Plastik, 'plastik'),
                     (Beton, 'beton')]

    nazwa = models.CharField(max_length=100, unique=True)
    rodzaj = models.CharField(max_length=100, choices=rodzaj_choices, null=True, default=Bd)
    wysokosc = models.DecimalField(max_digits=3, decimal_places=0, null=True, help_text="podaj bez przcecinków przybliżoną wysokość")
    ilosc_drog = models.CharField(max_length=15, choices=ilosc_drog_choices, default=Bd)
    opis = models.TextField(max_length=1000, default='uzupełnij', help_text="tutaj wpisz dłuższy opis miejsca")
    wyceny = models.CharField(max_length=15, choices=wyceny_choices, default="bd")
    skala = models.CharField(max_length=30, choices=skala_choices, default="bd")
    wiek_skal = models.CharField(max_length=100, default = '', blank=True)
    facja = models.CharField(max_length=100, default = '', blank=True)
    rejon = models.CharField(max_length=100, default = '', blank=True)
    nazwa_alt = models.CharField(max_length=100, default = '', blank=True)
    rodzaj_alt = models.CharField(max_length=100, choices=rodzaj_choices, null=True, default=Bd)
    rejon_dod = models.CharField(max_length=100, default = '', blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    def __str__(self):
        return self.nazwa

#linki do stron internetowych
class Site(models.Model):
    nazwa_strony = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie")
    link = models.URLField(max_length=200)
    ocena = models.CharField(max_length=1, help_text="skala od 1 do 5")
    crags = models.ForeignKey(Crag, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazwa_strony}'

class Movie(models.Model):
    nazwa_filmu = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie")
    link = models.URLField(max_length=200)
    crags = models.ForeignKey(Crag, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazwa_filmu}'

#nazwy topo
class Topo(models.Model):

    nazwa_topo = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie")
    autor = models.CharField(max_length=200)
    crags = models.ForeignKey(Crag, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazwa_topo}'
