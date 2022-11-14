
from django import forms

class FormularioEmpleados(forms.Form):

    EMPLEADOS = (
            (1, 'Cheff'),
            (2, 'Administrador'),
            (3, 'Mesero'),
            (4, 'Ayudante'),

    )
    nombre = forms.CharField(
            required=True,
            max_length=15,
            widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )

    apellidos = forms.CharField(
            required=True,
            max_length=15,
            widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )

    foto = forms.CharField(
            required=True,
            widget=forms.Textarea(attrs={'class': 'form-control mb-3'})

    )
    cargo= forms.ChoiceField(
            required=True,      
            widget=forms.Select(attrs={'class': 'form-control mb-3'}),
            choices=EMPLEADOS
    )
