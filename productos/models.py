from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    email_proveedor = models.EmailField()

    def __str__(self):
        return self.nombre