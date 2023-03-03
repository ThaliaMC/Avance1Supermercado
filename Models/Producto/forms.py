
from django import forms
from django.forms import ModelForm

from Models.Producto.models import Producto


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {'fecha_vencimiento' : forms.DateInput(attrs={'type':'date'}),'fecha_entrada' : forms.DateInput(attrs={'type':'date'})}


