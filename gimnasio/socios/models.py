from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    horario = models.DateTimeField()
    cupo_maximo = models.PositiveIntegerField(default=20)
    
    # Un entrenador puede dar muchas clases (ForeignKey)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='clases')
    
    # Una clase tiene muchos socios y un socio puede ir a muchas clases (ManyToManyField)
    socios = models.ManyToManyField(Socio, related_name='clases_inscritas', blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.horario}"
    
    def cupo_disponible(self):
        return self.cupo_maximo - self.socios.count()