from .models import Mensaje
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	mensajes = serializers.PrimaryKeyRelatedField(many=True, queryset=Mensaje.objects.all())

	class Meta:
		model=User
		fields=['id', 'username', 'mensajes']

class MensajeSerializer(serializers.ModelSerializer):
	usuario =  serializers.CharField(source='owner.username', read_only=True)
	class Meta:
		model=Mensaje
		fields=['id', 'message', 'url','deleted', 'usuario']