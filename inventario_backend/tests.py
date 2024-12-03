from django.test import TestCase
from .models import Producto, Categoria

class ProductoModelTest(TestCase):

    def setUp(self):
        # Crear una categoría de ejemplo
        self.categoria = Categoria.objects.create(
            nombre_categoria="Electrónica",
            descripcion_categoria="Productos electrónicos"
        )

    def test_crear_producto(self):
        # Crear un producto asociado a la categoría
        producto = Producto.objects.create(
            nombre_Producto="Smartphone",
            descripcion_Producto="Teléfono inteligente",
            precio_Producto=599.99,
            stock=10,
            categoria=self.categoria
        )
        self.assertEqual(producto.nombre_Producto, "Smartphone")
        self.assertEqual(producto.categoria.nombre_categoria, "Electrónica")

    def test_stock_alerta(self):
        # Simula un producto con bajo stock
        producto = Producto.objects.create(
            nombre_Producto="Cámara",
            descripcion_Producto="Cámara digital",
            precio_Producto=299.99,
            stock=2,
            categoria=self.categoria
        )
        self.assertTrue(producto.stock < 3, "El stock debería ser menor a 3 para generar una alerta")
