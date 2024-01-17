from django.db import models


#klasa Crag jest główną, obsługującą punkty na mapie. Pozostałe klasy są relacyjne dla Crag.
class Crag(models.Model):


    Trudnosci = [
        ('bd', 'uzupełnij'),
        ('łatwe', 'Łatwe'),
        ('średnie', 'Średnie'),
        ('trudne', 'Trudne'),
        ('zróżnicowane', 'Zróżnicowane')
    ]

    Ilosc_drog = [
        ('bd','uzupełnij'),
        ('mały','<20'),
        ('średni','20-100'),
        ('duży','>100')
    ]
    
    # Rodzaje = [
    #     ('bd','uzupełnij'),
    #     ('sport','Drogi sportowe'),
    #     ('bulder','Bulder'),
    #     ('trad','Trad'),
    #     ('ścianka','Ścianka wspinaczkowa')
    # ]
    
    nazwa = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    bulder = models.CharField(max_length=1, help_text="0 - droga, 1 - bulder, 2 - inne")
    #bulder zmień na:
    #rodzaj = models.Charfield(max_length=100, choices=rodzaj,default='bd')
    opis = models.TextField(default='uzupełnij', help_text="tutaj wpisz dłuższy opis miejsca")
    wyceny = models.CharField(max_length=15, choices=Trudnosci, default="bd")
    skala = models.CharField(max_length=100, default="uzupełnij", help_text="pojedyncza nazwa - np. piaskowiec, granit, wapień")
    wysokosc = models.DecimalField(max_digits=3, decimal_places=0, null=True, help_text="podaj bez przcecinków przybliżoną wysokość")
    ilość_dróg = models.CharField(max_length=10, choices=Ilosc_drog, default='bd')
    #dodaj wiek skały
    #wiek_skały = models.CharField(max_length=15, default='bd')
    def __str__(self):
        return self.nazwa

#linki do stron internetowych
class Site(models.Model):
    nazwa_strony = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie")
    link = models.URLField(max_length=200)
    ocena = models.CharField(max_length=1, help_text="skala od 1 do 5")
    crags = models.ForeignKey(Crag, null=True, on_delete=models.CASCADE)

class Route(models.Model):

    nazwa_drogi = models.CharField(max_length=200, default="brak")
    rejon = models.ForeignKey(Crag, on_delete=models.CASCADE, default="brak", null=True)

class Movie(models.Model):
    nazwa_filmu = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie")
    link = models.URLField(max_length=200)
    crags = models.ForeignKey(Crag, null=True, on_delete=models.CASCADE)
    nazwa_drogi = models.ForeignKey(Route, blank=True, on_delete=models.CASCADE, default="brak", null=True)

    def __str__(self):
        return f'{self.nazwa_filmu}'

#nazwy topo
class Topo(models.Model):

    nazwa_topo = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie")
    autor = models.CharField(max_length=200)
    crags = models.ForeignKey(Crag, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazwa_strony} {self.crags}'
