from django.urls import path
from .views import UserApiView
from .views import StoryApiView

urlpatterns = [
    # Rutas de los usuarios
    path('usuarios/list/', UserApiView.as_view(), name='list_usuarios'),
    path('usuarios/crear-usuario/', UserApiView.as_view(), name='crear_usuario'),
    path('usuarios/editar-usuario/<int:pkid>/', UserApiView.as_view(), name='editar_usuario'), 
    path('usuarios/eliminar-usuario/<int:pkid>/', UserApiView.as_view(), name='eliminar_usuario'),  
    path('usuarios/getUsuario/<int:pkid>/', UserApiView.as_view(), name='get_usuario'),  

    # Rutas de las publicaciones
    path('publicaciones/list/', StoryApiView.as_view(), name='list_publicaciones'),  # Lista todas las publicaciones
    path('publicaciones/crear-publicacion/', StoryApiView.as_view(), name='crear_publicacion'),  # Crea una nueva publicación
    path('publicaciones/editar-publicacion/<int:pkid>/', StoryApiView.as_view(), name='editar_publicacion'),  # Edita una publicación específica
    path('publicaciones/eliminar-publicacion/<int:pkid>/', StoryApiView.as_view(), name='eliminar_publicacion'),  # Elimina una publicación específica
    path('publicaciones/getPublicacion/<int:pkid>/', StoryApiView.as_view(), name='get_publicacion'),  # Obtiene una publicación específica
]

