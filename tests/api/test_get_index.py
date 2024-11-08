from http import HTTPStatus


def test_get_index(client):
    res = client.get('/')
    assert res.status_code == HTTPStatus.OK
