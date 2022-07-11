from tkinter import CASCADE
from django.db import models

# Create your models here.

# 1-. Se crea el modelo Cliente
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name='Identificador de cliente')
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre del cliente')
    apellidos = models.CharField(max_length=150, null=False, verbose_name='Apellido del cliente')
    correo = models.CharField(max_length=200, null=False, verbose_name='Correo del cliente')
    direccion = models.CharField(max_length=200, null=True, verbose_name='Dirección del cliente')

    def __str__(self):
        return 'Ingresado cliente: '+ self.nombre + ' ' +self.apellidos

# 2-. Se crea el modelo Producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, verbose_name= 'Identificador de producto')
    nom_producto = models.CharField(max_length=100, null=False, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=250, null=True, verbose_name='Descripción del producto')
    precio = models.IntegerField(null=False, verbose_name='Precio del producto')

    def __str__(self):
        return 'Nombre del producto: ' + self.nom_producto

# 3-. Se crea el modelo MedioPago
class MedioPago(models.Model):
    id_medio_pago = models.AutoField(primary_key=True, verbose_name= 'Identificador del medio de pago')
    nom_med_pago = models.CharField(max_length=25, null=False, verbose_name='Nombre medio de pago')

    def __str__(self):
        return 'Pagó con: '+ self.nom_med_pago


# 4-. Se crea el modelo Venta
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True, verbose_name='Identificador de venta')
    monto = models.IntegerField(null=False, verbose_name='Monto total')
    fecha = models.CharField(max_length=10, null=False, verbose_name='Fecha de la venta')
    medio_pago = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return 'Venta N°: '+ str(self.id_venta)


# 5-. Se crea el modelo DetalleVenta
class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True, verbose_name=' Identificador del detalle de venta')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

    def __str__(self):
        return 'Detalle de venta N°: '+ str(self.id_detalle_venta)




