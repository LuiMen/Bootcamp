from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from apps.book.models import Book


@receiver(post_save, sender=Book)
def book_post_save(sender, instance, created, **kwargs):
    print('Saved book')
    for author in instance.authors.all():
        page_count = 0
        for book in author.book_set.all():
            page_count += book.pages
        author.total_pages = page_count
        author.save()
