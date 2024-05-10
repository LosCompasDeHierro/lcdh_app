from django.db import models
from django_prose_editor.sanitized import SanitizedProseEditorField

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, unique=True,verbose_name = "Nombre de páis")
    sectionname = models.SlugField(max_length=50, verbose_name = "Identificador del apartado (debe ser una sola palabra)")

    def __str__(self):
        return str(self.name)

    class Meta:
        # ordering = ["name"]
        verbose_name = "País"
        verbose_name_plural = "Países"


class Celula(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name = "País")
    name = models.CharField(max_length=100, verbose_name = "Nombre de la célula")
    description = SanitizedProseEditorField(max_length=10000, blank=True, verbose_name = "Descripción") # max_length=10000, blank=True
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='celulas', blank=True)
    hideInMainPage = models.BooleanField(default=False, verbose_name = "Ocultar de la página principal")
    representante = models.OneToOneField("Compa", on_delete=models.SET_NULL, null=True, blank=True, related_name='representante_del_mesfk')
    staff = models.ForeignKey("Compa", on_delete=models.SET_NULL, null=True, blank=True, related_name='stafffk')
    compaDelMes = models.OneToOneField("Compa", on_delete=models.SET_NULL, null=True, blank=True, related_name='compa_del_mesfk')

    def __str__(self):
        return self.country.name + ' - ' + self.name

    class Meta:
        ordering = ["country","name"]
        verbose_name = "Célula"
        verbose_name_plural = "Células"

class CategoriaProfesion(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Nombre de la categoría de profesión")

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoría de Profesión"
        verbose_name_plural = "Categorías de Profesiones"

class Profesion(models.Model):
    categoriaProfesion = models.ForeignKey(CategoriaProfesion, on_delete=models.SET_NULL, null=True, verbose_name="Categoría de la profesión")
    name = models.CharField(max_length=100, verbose_name = "Nombre de la profesión")
    oficio = models.BooleanField(default=False, verbose_name = "¿Esta profesión es un oficio?")

    def __str__(self):
        return self.categoriaProfesion.name + " - " + str(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name = "Profesión"
        verbose_name_plural = "Profesiones"

class Compa(models.Model):
    celula = models.ForeignKey(Celula, on_delete=models.CASCADE, null=True, verbose_name = "Célula")
    edad = models.IntegerField(blank=True, default=0, verbose_name = "Edad del compa")
    sexo = models.CharField(max_length=1, blank=True, default='M', verbose_name="Sexo del compa")
    nickname = models.CharField(max_length=100, blank=True, verbose_name = "Apodo del compa")
    name = models.CharField(max_length=100, verbose_name = "Nombre del compa")
    picture = models.ImageField(upload_to='celulas', blank=True, verbose_name = "Foto del compa")
    profession = models.ForeignKey(Profesion, on_delete=models.SET_NULL, null=True, verbose_name = "Profesión del compa")
    biografia = SanitizedProseEditorField(max_length=10000, blank=True, verbose_name="Biografía pública")
    testimonio = SanitizedProseEditorField(max_length=10000, blank=True, verbose_name="Testimonio público")
    notas = SanitizedProseEditorField(max_length=10000, blank=True, verbose_name="Notas privadas")

    def __str__(self):
        return str(self.nickname)

class Anuncio(models.Model):
    celula = models.ForeignKey(Celula, on_delete=models.CASCADE, null=True, verbose_name = "Célula")
    alt = models.CharField(max_length=200, verbose_name = "Nombre descriptivo del anuncio")
    image = models.ImageField(upload_to='celulas', blank=True, verbose_name = "Imágen")
    text = models.CharField(max_length=100, blank=True, verbose_name = "Texto a mostrar del lado derecho")

    def __str__(self):
        return self.celula.name + ' - ' + self.alt

class AsistenciaCompaCelula(models.Model):
    compa = models.ForeignKey(Compa, on_delete=models.CASCADE, null=True, verbose_name = "Compa")
    celula = models.ForeignKey(Celula, on_delete=models.CASCADE, null=True, verbose_name = "Célula")
    attendance = models.IntegerField(default=0, verbose_name = "Asistencia anual")