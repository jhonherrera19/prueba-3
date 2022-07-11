from django import forms
from django.forms import ModelForm

#1-.Llamar modelo Cliente
from .models import Cliente, Producto, MedioPago, Venta, DetalleVenta

#1-. Crear la clase cliente para el formulario desde la bbdd
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['id_cliente','nombre','apellidos','correo','direccion']

#2-. Crear la clase producto para el formulario desde la bbdd
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto','nom_producto','descripcion','precio']

#3-. Crear la clase medio de pago para el formulario desde la bbdd
class MedioPagoForm(ModelForm):
    class Meta:
        model = MedioPago
        fields = ['id_medio_pago','nom_med_pago']

#4-. Crear la clase medio de pago para el formulario desde la bbdd
class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = ['id_venta','monto','fecha','medio_pago','cliente']

#4-. Crear la clase medio de pago para el formulario desde la bbdd
class DetalleVentaForm(ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['id_detalle_venta','producto','venta']