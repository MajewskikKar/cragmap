from django.db import models


#klasa Crag jest główną, obsługującą punkty na mapie. Pozostałe klasy są relacyjne dla Crag.
class Crag(models.Model):

    EASY = 'łatwe'
    MEDIUM = 'średnie'
    HARD = 'trudne'
    DEF = 'zróżnicowane'

    Trudnosci = [
        (EASY, 'Łatwe'),
        (MEDIUM, 'Średnie'),
        (HARD, 'Trudne'),
        (DEF, 'Zróżnicowane')
    ]
    nazwa = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    bulder = models.CharField(max_length=1, help_text="0 - droga, 1 - bulder, 2 - inne")
    opis = models.TextField(default='uzupelnij', help_text="tutaj wpisz dłuższy opis miejsca")
    wyceny = models.CharField(max_length=15, choices=Trudnosci, default="uzupelnij")
    skala = models.CharField(max_length=100, default="uzupelnij", help_text="pojedyncza nazwa - np. piaskowiec, granit, wapień")

    def __str__(self):
        return self.nazwa

#linki do stron internetowych
class Site(models.Model):

    nazwa_strony = models.CharField(max_length=100, help_text="Nazwa która będzie wyświetlała się w popupie")
    link = models.URLField(max_length=200)
    ocena = models.CharField(max_length=1, help_text="skala od 1 do 5")
    crags = models.ForeignKey(Crag, null=True, on_delete=models.CASCADE)


#filmiki z internetu
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
        return f'{self.nazwa_strony} {self.crags}'
