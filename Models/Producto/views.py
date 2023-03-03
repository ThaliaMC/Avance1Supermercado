from django.http import HttpRequest
from django.shortcuts import render


from Models.Producto.forms import FormularioProducto

# Create your views here.

class FormularioProductoView(HttpRequest):

    def index(request):
        producto = FormularioProducto()
        return render(request,"ProductoIndex.html",{"form":producto})
    
    def procesar_formulario(request):
        producto = FormularioProducto(request.POST)
        if producto.is_valid():
            producto.save()
            producto = FormularioProducto()

        return render(request,"ProductoIndex.html",{"form": producto, "mensaje":'OK'})
    
    
