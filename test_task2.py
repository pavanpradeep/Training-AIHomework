import pytest
from task2 import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client



def test_info_api(client):

    rv = client.get('/api/v1/info')
    print(rv.data)
    assert b'{"Receiver": "Cisco is the best!"}' in rv.data