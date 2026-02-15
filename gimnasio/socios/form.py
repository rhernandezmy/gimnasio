from django import forms
from .models import Socio
from django.core.exceptions import ValidationError

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'apellidos', 'email', 'telefono', 'fecha_nacimiento', 'activo']  
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),  # Para usar un selector de fecha en el formulario
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Socio.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El número de teléfono debe contener solo dígitos.")
        return telefono
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.isalpha():
            raise forms.ValidationError("El nombre debe contener solo letras.")
        return nombre
    
    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos')
        if not all(apellido.isalpha() for apellido in apellidos.split()):
            raise forms.ValidationError("Los apellidos deben contener solo letras.")
        return apellidos
    
    def clean_activo(self):
        activo = self.cleaned_data.get('activo')
        if activo is None:
            raise forms.ValidationError("El campo 'activo' es obligatorio.")
        return activo  
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento and fecha_nacimiento > forms.fields.datetime.date.today():
            self.add_error('fecha_nacimiento', "La fecha de nacimiento no puede ser en el futuro.")
        nombre = cleaned_data.get('nombre')
        apellidos = cleaned_data.get('apellidos')
        if nombre and apellidos:
            if Socio.objects.filter(nombre=nombre, apellidos=apellidos).exists():
                raise forms.ValidationError("Ya existe un socio con este nombre y apellidos.")
        return cleaned_data

    