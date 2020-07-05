import pytest
from library_api import models as library_models


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        library_models.Language.objects.update_or_create(name='ENG')
