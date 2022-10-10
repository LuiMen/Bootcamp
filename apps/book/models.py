from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    publication_date = models.DateField(verbose_name='Fecha de Publicación')
    pages = models.PositiveSmallIntegerField(verbose_name='Número de páginas')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, verbose_name='Categoría')

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return '%s (%s)' % (self.title, self.publication_date.year)
