from django.contrib import admin
from.models import Cliente, Producto, MedioPago, Venta, DetalleVenta
# Register your models here.
#Permite administrar el modelo completo

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(MedioPago)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
