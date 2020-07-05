from django.conf import settings
from post_office import mail
from library_api import models as library_models


def notify_all_new_book(book: library_models.Book):
    mail.send(
        recipients=list(library_models.Follower.objects.values_list('email', flat=True)),
        sender=settings.LIBRARY_EMAIL,
        subject='New book is allowed',
        message='Book name: {}'.format(book.name),
    )
