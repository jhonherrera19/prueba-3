from django.shortcuts import render, redirect

from core.forms import ClienteForm, ProductoForm, MedioPagoForm, VentaForm, DetalleVentaForm
#1-.Llamar modelo Cliente
from.models import Cliente, Producto, MedioPago, Venta, DetalleVenta

# Create your views here.

#------
def home (request):
    return render(request, 'core/home.html')
#------

#CRUD 1: CLIENTE
#A-. Listar o READ.
#B-. Crear o CREATE.
#C-. Modificar o UPDATE.
#D-. Borrar o DELETE.

#A
def home_cliente(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request, 'core/home_cliente.html', datos)

#B
def form_cliente(request):
    datos = {
        'form' : ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] ="Guardados correctamente"
    return render(request, 'core/form_cliente.html', datos)


#C
def form_mod_cliente(request,id):
    cliente = Cliente.objects.get(id_cliente=id)
    datos = {
        'form' : ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid:
            formulario.save()
            cliente = Cliente.objects.get(id_cliente=id)
            datos = {
            'form' : ClienteForm(instance=cliente)
            }       
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_cliente.html', datos)



#D
def form_del_cliente(request, id):
    cliente = Cliente.objects.get(id_cliente=id)
    cliente.delete()
    return redirect(to="home")

#--------------------------------------------------------------------

#CRUD 2: PRODUCTO
#A-. Listar o READ.
#B-. Crear o CREATE.
#C-. Modificar o UPDATE.
#D-. Borrar o DELETE.

#A
def home_producto(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/home_producto.html', datos)

#B
def form_producto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] ="Guardados correctamente"
    return render(request, 'core/form_producto.html', datos)

#C
def form_mod_producto(request,id):
    producto = Producto.objects.get(id_producto=id)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            producto = Producto.objects.get(id_producto=id)
            datos = {
            'form' : ProductoForm(instance=producto)
            }       
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_producto.html', datos)

#D
def form_del_producto(request, id):
    producto = Producto.objects.get(id_producto=id)
    producto.delete()
    return redirect(to="home")

#--------------------------------------------------------------------

#CRUD 3: MEDIO DE PAGO
#A-. Listar o READ.
#B-. Crear o CREATE.
#C-. Modificar o UPDATE.
#D-. Borrar o DELETE.

#A
def home_medioPago(request):
    medioPagos = MedioPago.objects.all()
    datos = {
        'medioPagos': medioPagos
    }
    return render(request, 'core/home_medioPago.html', datos)

#B
def form_medioPago(request):#En un inicio
    datos = {
        'form' : MedioPagoForm()
    }
    if request.method == 'POST':
        formulario = MedioPagoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] ="Guardados correctamente"
    return render(request, 'core/form_medioPago.html', datos)

#C
def form_mod_medioPago(request,id):
    medioPago = MedioPago.objects.get(id_medio_pago=id)
    datos = {
        'form' : MedioPagoForm(instance=medioPago)
    }
    if request.method == 'POST':
        formulario = MedioPagoForm(data=request.POST, instance=medioPago)
        if formulario.is_valid:
            formulario.save()
            medioPago = MedioPago.objects.get(id_medio_pago=id)
            datos = {
            'form' : MedioPagoForm(instance=medioPago)
            }       
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_medioPago.html', datos)

#D
def form_del_medioPago(request, id):
    medioPago = MedioPago.objects.get(id_medio_pago=id)
    medioPago.delete()
    return redirect(to="home")

#--------------------------------------------------------------------

#CRUD 4: VENTA
#A-. Listar o READ.
#B-. Crear o CREATE.
#C-. Modificar o UPDATE.
#D-. Borrar o DELETE.

#A
def home_venta(request):
    ventas = Venta.objects.all()
    datos = {
        'ventas': ventas
    }
    return render(request, 'core/home_venta.html', datos)

#B
def form_venta(request):
    datos = {
        'form' : VentaForm()
    }
    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] ="Guardados correctamente"
    return render(request, 'core/form_venta.html', datos)


#C
def form_mod_venta(request,id):
    venta = Venta.objects.get(id_venta=id)
    datos = {
        'form' : VentaForm(instance=venta)
    }
    if request.method == 'POST':
        formulario = VentaForm(data=request.POST, instance=venta)
        if formulario.is_valid:
            formulario.save()
            venta = Venta.objects.get(id_venta=id)
            datos = {
            'form' : MedioPagoForm(instance=venta)
            }       
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_venta.html', datos)

#D
def form_del_venta(request, id):
    venta = Venta.objects.get(id_venta=id)
    venta.delete()
    return redirect(to="home")

#--------------------------------------------------------------------

#CRUD 4: DETALLE DE VENTA
#A-. Listar o READ.
#B-. Crear o CREATE.
#C-. Modificar o UPDATE.
#D-. Borrar o DELETE.

#A
def home_detalleVenta(request):
    detalleVentas = DetalleVenta.objects.all()
    datos = {
        'detalleVentas': detalleVentas
    }
    return render(request, 'core/home_detalleVenta.html', datos)

#B
def form_detalleVenta(request):
    datos = {
        'form' : DetalleVentaForm()
    }
    if request.method == 'POST':
        formulario = DetalleVentaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] ="Guardados correctamente"
    return render(request, 'core/form_detalleVenta.html', datos)


#C
def form_mod_detalleVenta(request,id):
    detalleVenta = DetalleVenta.objects.get(id_detalle_venta=id)
    datos = {
        'form' : VentaForm(instance=detalleVenta)
    }
    if request.method == 'POST':
        formulario = DetalleVentaForm(data=request.POST, instance=detalleVenta)
        if formulario.is_valid:
            formulario.save()
            detalleVenta = DetalleVenta.objects.get(id_detalle_venta=id)
            datos = {
            'form' : DetalleVentaForm(instance=detalleVenta)
            }       
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_detalleVenta.html', datos)

#D
def form_del_detalleVenta(request, id):
    detalleVenta = DetalleVenta.objects.get(id_detalle_venta=id)
    detalleVenta.delete()
    return redirect(to="home")