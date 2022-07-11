from django.urls import path
from rest_venta.views import lista_ventas, lista_mediosDePago, lista_detalleVenta, detalle_venta, detalle_medioDePago, detalle_detalleVenta

urlpatterns = [
    path('lista_ventas', lista_ventas, name= "lista_ventas"),
    path('lista_mediosDePago', lista_mediosDePago, name= "lista_mediosDePago"),
    path('lista_detalleVenta', lista_detalleVenta, name= "lista_detalleVenta"),
    path('detalle_venta/<id>', detalle_venta, name = "detalle_venta"),
    path('detalle_medioDePago/<id>', detalle_medioDePago, name = "detalle_medioDePago"),
    path('detalle_detalleVenta/<id>', detalle_detalleVenta, name = "detalle_detalleVenta"),
]