from django.shortcuts import render
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Mensaje
from .serializers import MensajeSerializer, UserSerializer
from rest_framework import status
from django.contrib.auth.models import User


#ms = mensaje serializer
#s = serializer
#mo = mensaje object
class MensajesList(views.APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		mensajes = Mensaje.objects.all()
		ms = MensajeSerializer(mensajes, many=True)
		return Response(ms.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		s = MensajeSerializer(data=request.data)
		if s.is_valid():
			s.save(owner=self.request.user)
			return Response(s.data, status=status.HTTP_201_CREATED)
		return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

class MensajesDetail(views.APIView):
	permission_classes = [IsAuthenticated]
	
	def get_object(self, pk):
		try:
			m = Mensaje.objects.get(pk=pk)
			return m
		except Mensaje.DoesNotExist:
			return Response({"mensaje":"Error"}, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, pk):
		us = UserSerializer(request.user) 
		usuarioActual = us.data
		if pk in usuarioActual['mensajes']:
			mensaje = self.get_object(pk)
			ms = MensajeSerializer(mensaje, data=request.data)
			if ms.is_valid():
				ms.save()
				return Response(ms.data, status=status.HTTP_200_OK)
			return Response({"error":"No es valido"},status=status.HTTP_400_BAD_REQUEST)
		return Response({"error":"No es el mismo usuario", "respuesta":None}, status=status.HTTP_400_BAD_REQUEST)
		

	def delete(self, request, pk):
		print(request.META.get('HTTP_X_MYHEADER'))
		return Response({"mensaje":"prueba delete"})

	def get(self, request, pk):
		try:
			mensaje = self.get_object(pk)
			ms = MensajeSerializer(mensaje)
			return Response(ms.data, status=status.HTTP_200_OK)
		except:
			return Response({"mensaje":"Error"}, status=status.HTTP_404_NOT_FOUND)


class UsuariosList(views.APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		usuarios = User.objects.all()
		us = UserSerializer(usuarios, many=True)
		return Response(us.data, status=status.HTTP_200_OK)

class UsuarioDetail(views.APIView):
	permission_classes = [IsAuthenticated]

	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			return Response({"mensaje":"El usuario no existe"}, status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk):
		try:
			usuario = self.get_object(pk)
			us = UserSerializer(usuario)
			return Response(us.data, status=status.HTTP_200_OK) 
		except:
			return Response({"mensaje":"Error"}, status=status.HTTP_404_NOT_FOUND)

class UsuarioActual(views.APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		s = UserSerializer(request.user)
		return Response(s.data, status=status.HTTP_200_OK)
