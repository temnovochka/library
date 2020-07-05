import pytest
from rest_framework.test import APIClient


def _query_api(obj, path):
    client = APIClient()

    post_response = client.post('/api/{}/'.format(path), obj)
    assert post_response.status_code == 201
    obj['id'] = post_response.data['id']

    get_response = client.get('/api/{}/{}/'.format(path, obj['id']))

    assert get_response.status_code == 200
    assert get_response.data == obj


@pytest.mark.django_db
def test_book_api():
    path = 'book'
    obj = {'name': 'Harry Potter', 'year': 2015, 'languages': ['ENG'], 'authors': []}
    _query_api(obj, path)


@pytest.mark.django_db
def test_follower_api():
    path = 'follower'
    obj = {'email': 'a@a.ru', 'last_name': 'a', 'first_name': 'b', 'middle_name': 'c'}
    _query_api(obj, path)
