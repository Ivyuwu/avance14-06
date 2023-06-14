from django.db import models
    
class Usuario(models.Model):
    ROL = (('Administrador', 'Administrador'),
    ('Funcionario', 'Funcionario'),
    ('Usuario', 'Usuario'),
    )
    nombre = models.CharField(max_length=50, null=True) 
    apellido = models.CharField(max_length=50, null=True)
    rut = models.CharField(max_length=13, null=True)
    correo = models.EmailField(max_length=50, null=True)
    rol = models.CharField(max_length=200, null=True, choices=ROL)

    def __str__(self):
        return self.nombre
