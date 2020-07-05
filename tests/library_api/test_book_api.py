import pytest

from rest_framework.test import APIClient


@pytest.mark.django_db
def test_book_api():
    client = APIClient()

    obj = {'name': 'Harry Potter', 'year': 2015, 'languages': ['ENG'], 'authors': []}
    post_response = client.post('/api/book/', obj)
    assert post_response.status_code == 201
    obj['id'] = post_response.data['id']

    get_response = client.get('/api/book/{}/'.format(obj['id']))

    assert get_response.status_code == 200
    assert get_response.data == obj
