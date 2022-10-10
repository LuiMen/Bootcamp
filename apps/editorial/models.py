from django.db import models

from apps.user.models import User


class Editorial(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

    def __str__(self):
        return self.name
