from django.db import models

# Create your models here.
class Socio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class Entrenador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class Clase(models.Model):
    # Definimos las opciones para el desplegable de tipo de clase
    TIPO_CLASES = [
        ('yoga', 'Yoga'),
        ('pilates', 'Pilates'),
        ('spinning', 'Spinning'),
        ('crossfit', 'CrossFit'),
        ('zumba', 'Zumba'),
        ('boxeo', 'Boxeo'),
    ]
    
    # Definimos los textos predeterminados para cada tipo de clase
    DESCRIPCIONES_PREDETERMINADAS = {
        'yoga': 'Clase de yoga para mejorar la flexibilidad y el bienestar.',
        'pilates': 'Clase de pilates para fortalecer el core y mejorar la postura.',
        'spinning': 'Clase de spinning para quemar calorías y mejorar la resistencia cardiovascular.',
        'crossfit': 'Clase de crossfit para entrenar fuerza y resistencia con ejercicios variados.',
        'zumba': 'Clase de zumba para divertirse bailando y quemar calorías al ritmo de la música.',
        'boxeo': 'Clase de boxeo para aprender técnicas de defensa personal y mejorar la condición física.',
    }
    
    nombre = models.CharField(max_length=100, choices=TIPO_CLASES)
    descripcion = models.TextField(blank=True, null=True)
    horario = models.DateTimeField()
    cupo_maximo = models.PositiveIntegerField(default=20)
    
    # Un entrenador puede dar muchas clases (ForeignKey) y una clase tiene un solo entrenador
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='clases')
    
    # Una clase tiene muchos socios y un socio puede ir a muchas clases (ManyToManyField)
    socios = models.ManyToManyField(Socio, related_name='clases_inscritas', blank=True)

    def __str__(self):
        return f"{self.get_nombre_display()} - {self.horario.strftime('%d/%m %H:%M')}"
    
    
    def cupo_disponible(self):
        # Usamos .all().count() para mayor precisión en tiempo real
        return self.cupo_maximo - self.socios.all().count()
    
    # Sobrescribimos el método save para asignar la descripción predeterminada según el tipo de clase
    def save(self, *args, **kwargs):
        # Asignamos SIEMPRE la descripción según el nombre elegido
        self.descripcion = self.DESCRIPCIONES_PREDETERMINADAS.get(self.nombre, 'Sin descripción.')
        super().save(*args, **kwargs)