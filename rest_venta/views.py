from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Venta, MedioPago, DetalleVenta
from .serializers import VentaSerializer, MedioPagoSerializer, DetalleVentaSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.LISTO
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_ventas(request):
    if request.method == 'GET':
        venta = Venta.objects.all()
        serializer = VentaSerializer(venta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_mediosDePago(request):
    if request.method == 'GET':
        medioPago = MedioPago.objects.all()
        serializer = MedioPagoSerializer(medioPago, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MedioPagoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_detalleVenta(request):
    if request.method == 'GET':
        detalleVenta = DetalleVenta.objects.all()
        serializer = DetalleVentaSerializer(detalleVenta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DetalleVentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_venta(request,id):
    try:
        venta = Venta.objects.get(id_venta=id)
    except Venta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VentaSerializer(venta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(venta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_medioDePago(request,id):
    try:
        medioDePago = MedioPago.objects.get(id_medio_pago=id)
    except MedioPago.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MedioPagoSerializer(medioDePago)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MedioPagoSerializer(medioDePago, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        medioDePago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_detalleVenta(request,id):
    try:
        detalleVenta = DetalleVenta.objects.get(id_detalle_venta=id)
    except DetalleVenta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DetalleVentaSerializer(detalleVenta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DetalleVentaSerializer(detalleVenta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        detalleVenta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


