import pytest

from rest_framework.test import APIClient


@pytest.mark.django_db
def test_follower_api():
    client = APIClient()

    obj = {'email': 'a@a.ru', 'last_name': 'a', 'first_name': 'b', 'middle_name': 'c'}
    post_response = client.post('/api/follower/', obj)
    assert post_response.status_code == 201
    obj['id'] = post_response.data['id']

    get_response = client.get('/api/follower/{}/'.format(obj['id']))

    assert get_response.status_code == 200
    assert get_response.data == obj
