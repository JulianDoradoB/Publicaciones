from django.db import models

# Crear tu modelo de usuario
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default="default_password")  # Considera usar hashing para las contraseñas
    nombre = models.CharField(max_length=50, default="Sin nombre")
    foto_perfil = models.URLField(blank=True, null=True)  # URL de la foto de perfil
    banner = models.URLField(blank=True, null=True)  # URL del banner
    educacion = models.TextField(blank=True, null=True)  # Información de educación
    habilidades = models.TextField(blank=True, null=True)  # Habilidades del usuario
    certificaciones = models.TextField(blank=True, null=True)  # Certificaciones del usuario

    def __str__(self):
        return self.nombre


# Modelo para las publicaciones (Story)
class Story(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)  # Asigna la fecha automáticamente al crear la publicación
    tipo = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, related_name='publicaciones', on_delete=models.CASCADE)  # Relación con el modelo User

    def __str__(self):
        return f"{self.tipo} - {self.contenido[:20]}"

    # Método para publicar la historia (si es necesario)
    def publicar(self):
        # Aquí puedes agregar la lógica de publicación si es necesario
        pass
