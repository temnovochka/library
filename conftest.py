import pytest
from library_api import models as library_models
from post_office.signals import email_queued


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        library_models.Language.objects.update_or_create(name='ENG')


@pytest.fixture(autouse=True)
def mute_signals(request):
    """
    Disable mailing signal while testing
    """
    receivers = email_queued.receivers
    email_queued.receivers = []

    def restore():
        email_queued.receivers = receivers

    request.addfinalizer(restore)
