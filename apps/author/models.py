from django.db import models

from apps.user.models import User


class Author(models.Model):
    alias = models.CharField(verbose_name='Alias', max_length=50)
    birth_date = models.DateField(verbose_name='Fecha de Nacimiento')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
