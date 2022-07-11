from rest_framework import serializers
from core.models import Venta, MedioPago, DetalleVenta

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id_venta','monto','fecha','medio_pago','cliente']

class MedioPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedioPago
        fields = ['id_medio_pago','nom_med_pago']

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['id_detalle_venta','producto','venta']

