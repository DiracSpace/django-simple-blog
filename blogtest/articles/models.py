from django.db import models

"""
Database management for articles

python3 manage.py makemigrations para generar el archivo nuevo de cambios
python3 manage.py migrate para aplicar cualquier cambio realizado aquí a la bd
"""
class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)

    # function for shell retrieval
    def __str__(self):
        return self.title
