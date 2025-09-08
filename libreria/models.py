from django.db import models

<<<<<<< HEAD
# Create your models here.
class Pelicula(models.Model):
    # pongo el id aunque no es necesario
    # el problema que no me insertaba registros era que yo hacía los inserts forzando los ids
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nombre_ingles = models.CharField(max_length=100, default="", blank=True, null=True)
    nombre_alternativo = models.CharField(max_length=100, default="", blank=True, null=True)
    anio = models.IntegerField(verbose_name="Año")
    imagen = models.CharField(max_length=50, verbose_name="Imagen", default="", blank=True, null=True)
    director = models.CharField(max_length=100, default="")
    actor_1 = models.CharField(max_length=100, default="", blank=True, null=True)
    actor_2 = models.CharField(max_length=100, default="", blank=True, null=True)
    actor_3 = models.CharField(max_length=100, default="", blank=True, null=True)
    actor_4 = models.CharField(max_length=100, default="", blank=True, null=True)
    actor_5 = models.CharField(max_length=100, default="", blank=True, null=True)
    actor_6 = models.CharField(max_length=100, default="", blank=True, null=True)
    pais = models.CharField(max_length=40, default="", blank=True, null=True)
    imdb = models.CharField(max_length=100, default="", blank=True, null=True)
    resenia = models.TextField(verbose_name="Reseña", blank=True, null=True)
    top10 = models.BooleanField(verbose_name="Top", default=False, null=True)
    imagenlocal = models.ImageField(upload_to='img/', verbose_name="ImagenLocal", null=True, blank=True)
    genero = models.CharField(max_length=40, default="", blank=True, null=True)
    subgenero1 = models.CharField(max_length=40, default="", blank=True, null=True)
    subgenero2 = models.CharField(max_length=40, default="", blank=True, null=True)
    subgenero3 = models.CharField(max_length=40, default="", blank=True, null=True)
    color = models.BooleanField(verbose_name="Color", default=False, null=True)
    vista = models.BooleanField(verbose_name="Vista", default=False, null=True)
    cajitavertical = models.ImageField(upload_to='img/', verbose_name="CajitaVertical", null=True, blank=True)
    imagen1 = models.ImageField(upload_to='img/', verbose_name="Imagen1", null=True, blank=True)
    imagen2 = models.ImageField(upload_to='img/', verbose_name="Imagen2", null=True, blank=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.nombre + " (" + str(self.anio) + ", " + self.director + ")"
        return fila

    def save(self, *args, **kwargs):
        # Si resenia es "", lo paso a None (NULL en BD)
        if self.resenia == "":
            self.resenia = None
        super().save(*args, **kwargs)
        
=======
class Capitulo(models.Model):
    # pongo el id aunque no es necesario
    # el problema que no me insertaba registros era que yo hacía los inserts forzando los ids
    id_capitulo = models.AutoField(primary_key=True)
    numero = models.IntegerField(verbose_name="Numero")
    temporada = models.IntegerField(verbose_name="Temporada")
    numero_temporada = models.IntegerField(verbose_name="Numero_de_temporada")
    fecha = models.CharField(max_length=10, default="")
    imdb = models.CharField(max_length=100, default="", blank=True, null=True)
    titulo_ingles = models.CharField(max_length=100)
    titulo_espaniol = models.CharField(max_length=100, default="", blank=True, null=True)
    imagen_vertical = models.ImageField(upload_to='libreria/static/img', verbose_name="Imagen_vertical", null=True, blank=True)
    imagen1_horizontal = models.ImageField(upload_to='libreria/static/img', verbose_name="Imagen1_horizontal", null=True, blank=True)
    imagen2_horizontal = models.ImageField(upload_to='libreria/static/img', verbose_name="Imagen2_horizontal", null=True, blank=True)
    visto = models.BooleanField(verbose_name="Vista", default=False, null=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.titulo_ingles + " (" + str(self.numero) + ")"
        return fila

>>>>>>> e98e131a351e6f2b66ae9bd1604893aa7b1cd48b
    # En el caso que tuviera una imagen guardada (versión anterior)
    #def delete(self, using=True, keep_parents=False):
    #    self.imagen.storage.delete(self.imagen.name)
    #    super().delete()


class Actor(models.Model):
<<<<<<< HEAD
    id = models.AutoField(primary_key=True)
    nombreactor = models.CharField(max_length=100)
    imagenactor = models.ImageField(upload_to='img/', verbose_name="ImagenActor", null=True)
    textoactor = models.TextField(verbose_name="TextoActor", blank=True, default="", null=True)
    tipo = models.CharField(max_length=40, default="", blank=True, null=True)
=======
    id_actor = models.AutoField(primary_key=True)
    nombreactor = models.CharField(max_length=100)
    imagenactor = models.ImageField(upload_to='libreria/static/img', verbose_name="ImagenActor", null=True)
    textoactor = models.TextField(verbose_name="TextoActor", blank=True, default="", null=True)
>>>>>>> e98e131a351e6f2b66ae9bd1604893aa7b1cd48b

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.nombreactor
        return fila    


<<<<<<< HEAD
class Director(models.Model):
    id = models.AutoField(primary_key=True)
    nombredirector = models.CharField(max_length=100)
    imagendirector = models.ImageField(upload_to='img/', verbose_name="ImagenDirector", null=True)
    textodirector = models.TextField(verbose_name="TextoDirector", blank=True, default="", null=True)
    tipo = models.CharField(max_length=40, default="", blank=True, null=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.nombredirector
        return fila    


class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    enlace = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    textocorto = models.TextField(verbose_name="TextoCorto", blank=True, default="", null=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.titulo
        return fila    
=======
class Invitado(models.Model):
    id_invitado = models.AutoField(primary_key=True)
    id_capitulo = models.IntegerField(verbose_name="id_capitulo")
    nombreinvitado = models.CharField(max_length=100)
    imageninvitado = models.ImageField(upload_to='libreria/static/img', verbose_name="ImagenInvitado", null=True)
    textoinvitado = models.TextField(verbose_name="TextoInvitado", blank=True, default="", null=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.nombreinvitado
        return fila    


class Review(models.Model):
    id_review = models.AutoField(primary_key=True)
    id_capitulo = models.IntegerField(verbose_name="id_capitulo")
    plot = models.TextField(verbose_name="Plot", blank=True, default="", null=True)
    textoreview = models.TextField(verbose_name="Textoreview", blank=True, default="", null=True)

    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = str(self.id_review) + " (" + str(self.id_capitulo) + ")"
        return fila
>>>>>>> e98e131a351e6f2b66ae9bd1604893aa7b1cd48b
