import pytest
import requests_mock
from unittest.mock import patch
from frontend_service.app import app
from storage_service.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data  

def test_submit(client):
    """Test the submit endpoint."""
    with requests_mock.Mocker() as m:
        m.post('http://localhost:5001/store-email', text='mock response')
        response = client.post('/submit', data={'name': 'Test Name', 'email': 'test@example.com'})
        assert response.status_code == 302

def test_admin(client):
    """Test the admin endpoint."""
    with requests_mock.Mocker() as m:
        m.get('http://localhost:5001/admin', json={'key': 'value'})  # Mock response as needed
        response = client.get('/admin')
        assert response.status_code == 200
   