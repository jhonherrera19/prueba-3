from django. urls import path
# Llamar la vista de home, form de todos los objetos.
from.views import home, home_cliente, form_cliente, form_mod_cliente, form_del_cliente, home_producto, form_producto, form_mod_producto, form_del_producto, home_medioPago, form_medioPago, form_mod_medioPago, form_del_medioPago, home_venta, form_venta, form_mod_venta, form_del_venta, home_detalleVenta, form_detalleVenta, form_mod_detalleVenta, form_del_detalleVenta

# Se agrega  el formulario en las urls.py
urlpatterns = [
    path('',home,name='home'),
    path('home_cliente', home_cliente, name="home_cliente"),
    path('form_cliente', form_cliente, name="form_cliente"),#FORMULARIO DE CREACIÓN CLIENTE
    path('form_mod_cliente/<id>', form_mod_cliente, name='form_mod_cliente'),#FORMULARIO DE MODIFICACIÓN CLIENTE
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),#FORMULARIO DE ELIMINACIÓN CLIENTE
    path('home_producto', home_producto, name="home_producto"),
    path('form_producto', form_producto, name="form_producto"),#FORMULARIO DE CREACIÓN PRODUCTO
    path('form_mod_producto/<id>', form_mod_producto, name='form_mod_producto'),#FORMULARIO DE MODIFICACIÓN PRODUCTO
    path('form_del_producto/<id>', form_del_producto, name="form_del_producto"),#FORMULARIO DE ELIMINACIÓN PRODUCTO
    path('home_medioPago', home_medioPago, name="home_medioPago"),
    path('form_medioPago', form_medioPago, name="form_medioPago"),#FORMULARIO DE CREACIÓN MEDIO DE PAGO
    path('form_mod_medioPago/<id>', form_mod_medioPago, name='form_mod_medioPago'),#FORMULARIO DE MODIFICACIÓN MEDIO DE PAGO
    path('form_del_medioPago/<id>', form_del_medioPago, name="form_del_medioPago"),#FORMULARIO DE ELIMINACIÓN MEDIO DE PAGO
    path('home_venta', home_venta, name="home_venta"),
    path('form_venta', form_venta, name="form_venta"),#FORMULARIO DE CREACIÓN VENTA
    path('form_mod_venta/<id>', form_mod_venta, name='form_mod_venta'),#FORMULARIO DE MODIFICACIÓN VENTA
    path('form_del_venta/<id>', form_del_venta, name="form_del_venta"),#FORMULARIO DE ELIMINACIÓN VENTA
    path('home_detalleVenta', home_detalleVenta, name="home_detalleVenta"),
    path('form_detalleVenta', form_detalleVenta, name="form_detalleVenta"),#FORMULARIO DE CREACIÓN DETALLE DE VENTA
    path('form_mod_detalleVenta/<id>', form_mod_detalleVenta, name='form_mod_detalleVenta'),#FORMULARIO DE MODIFICACIÓN DETALLE DE VENTA
    path('form_del_detalleVenta/<id>', form_del_detalleVenta, name="form_del_detalleVenta"),#FORMULARIO DE ELIMINACIÓN DETALLE DE VENTA
]
