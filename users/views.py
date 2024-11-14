from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

class UserApiView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener la lista de usuarios
        lista_usuarios = User.objects.all()
        serializer_usuarios = UserSerializer(lista_usuarios, many=True)
        return Response(serializer_usuarios.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        # Crear un nuevo usuario
        data = {
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'nombre': request.data.get('nombre'),
            'foto_perfil': request.data.get('foto_perfil'),
            'banner': request.data.get('banner'),
            'educacion': request.data.get('educacion'),
            'habilidades': request.data.get('habilidades'),
            'certificaciones': request.data.get('certificaciones')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid, *args, **kwargs):
        # Editar un usuario existente
        try:
            mi_usuario = User.objects.get(id=pkid)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(mi_usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pkid):
        # Eliminar un usuario
        try:
            user_to_delete = User.objects.get(id=pkid)
            user_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def get_usuario(self, request, pkid, *args, **kwargs):
        # Obtener un usuario específico
        try:
            mi_usuario = User.objects.get(id=pkid)
            serializer_usuarios = UserSerializer(mi_usuario)
            return Response(serializer_usuarios.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Story
from .serializer import StorySerializer

class StoryApiView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener la lista de publicaciones
        lista_publicaciones = Story.objects.all()
        serializer_publicaciones = StorySerializer(lista_publicaciones, many=True)
        return Response(serializer_publicaciones.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        # Crear una nueva publicación
        data = {
            'contenido': request.data.get('contenido'),
            'fecha': request.data.get('fecha'),
            'tipo': request.data.get('tipo'),
            'usuario': request.data.get('usuario')
        }
        serializer = StorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid, *args, **kwargs):
        # Editar una publicación existente
        try:
            mi_publicacion = Story.objects.get(id=pkid)
        except Story.DoesNotExist:
            return Response({'error': 'Publicación no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StorySerializer(mi_publicacion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pkid):
        # Eliminar una publicación
        try:
            publicacion_to_delete = Story.objects.get(id=pkid)
            publicacion_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Story.DoesNotExist:
            return Response({'error': 'Publicación no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

    def get_publicacion(self, request, pkid, *args, **kwargs):
        # Obtener una publicación específica
        try:
            mi_publicacion = Story.objects.get(id=pkid)
            serializer_publicacion = StorySerializer(mi_publicacion)
            return Response(serializer_publicacion.data, status=status.HTTP_200_OK)
        except Story.DoesNotExist:
            return Response({'error': 'Publicación no encontrada.'}, status=status.HTTP_404_NOT_FOUND)


