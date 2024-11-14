from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'nombre', 'foto_perfil', 'banner', 'educacion', 'habilidades', 'certificaciones')

from rest_framework import serializers
from .models import Story, User

class StorySerializer(serializers.ModelSerializer):
    # Usuario debe ser un campo obligatorio para que lo incluya en el post
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Story
        fields = ('id', 'contenido', 'fecha', 'tipo', 'usuario')

    def validate_usuario(self, value):
        # Validación explícita de que el usuario existe
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El usuario no existe.")
        return value