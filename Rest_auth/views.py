from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt #No se va a implementar, ya que va a utilizar un método POST 
from django.contrib.auth.models import User # CON ESTA LÍNEA NO ES NECESARIO LA IMPLEMENTACIÓN DEL MODELO PARA LA BBDD.
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def login(request):
    try:
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
    except:
        return Response("No se encontró usuario")
        
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return Response("Usuario no existe")
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Password incorrecta")
    
    token, created = Token.objects.get_or_create(user = user)
    return Response(token.key)
