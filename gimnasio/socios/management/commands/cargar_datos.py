from django.core.management.base import BaseCommand
from socios.models import Socio, Entrenador, Clase
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Carga datos de prueba para el gimnasio'

    def handle(self, *args, **kwargs):
        self.stdout.write("Cargando datos...")

        # 1. Crear Entrenadores
        entrenadores_nombres = [
            ('Alex', 'Pro', 'CrossFit'),
            ('Marta', 'Zen', 'Yoga'),
            ('Carlos', 'Punch', 'Boxeo')
        ]
        
        entrenadores_objs = []
        for nom, ape, esp in entrenadores_nombres:
            e, _ = Entrenador.objects.get_or_create(
                nombre=nom, apellidos=ape, 
                email=f"{nom.lower()}@gym.com",
                especialidad=esp
            )
            entrenadores_objs.append(e)

        # 2. Crear Socios
        for i in range(1, 11):
            Socio.objects.get_or_create(
                nombre=f"Socio{i}",
                apellidos=f"Apellido{i}",
                email=f"socio{i}@correo.com",
                activo=True
            )

        # 3. Crear Clases
        tipos = ['yoga', 'crossfit', 'boxeo', 'spinning']
        for t in tipos:
            clase, _ = Clase.objects.get_or_create(
                nombre=t,
                horario=timezone.now() + timezone.timedelta(days=random.randint(1, 5)),
                entrenador=random.choice(entrenadores_objs),
                cupo_maximo=15
            )
            # Inscribir a 3 socios aleatorios en cada clase
            socios = Socio.objects.all()[:3]
            clase.socios.set(socios)

        self.stdout.write(self.style.SUCCESS('¡Datos cargados con éxito!'))
