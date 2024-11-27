from django.db import models

class Usuario(models.Model):
    ROLES = [
        ('admin', 'Administrador'),
        ('cliente', 'Cliente'),
    ]
    nombre_usuario = models.CharField(max_length=30, unique=True)
    contrasena_usuario = models.CharField(max_length=100)
    rol = models.CharField(max_length=10, choices=ROLES)

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)
    descripcion_categoria = models.TextField()

class Marca(models.Model):
    nombre_marca = models.CharField(max_length=30)

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=30)
    descripcion_producto = models.TextField()
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
