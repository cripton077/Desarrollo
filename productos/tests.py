from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .forms import ProductoForm

class ProductoFormTest(TestCase):
    def test_precio_invalido_negativo(self):
        form = ProductoForm(data={
            'nombre': 'Teclado Gamer',
            'precio': -5000,
            'email_proveedor': 'contacto@tienda.cl'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('precio', form.errors)

    def test_producto_valido(self):
        form = ProductoForm(data={
            'nombre': 'Mouse Pad',
            'precio': 12000,
            'email_proveedor': 'contacto@tienda.cl'
        })
        self.assertTrue(form.is_valid())