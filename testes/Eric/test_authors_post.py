import requests
import pytest
from config import AUTHORS_ENDPOINT

NEW_AUTHOR_DATA = {
    "id": 101,
    "idBook": 1,
    "firstName": "Autor",
    "lastName": "Teste Manus"
}

def test_tc33_create_new_author_success():
    """TC33: Criar novo Author (POST /Authors)"""
    response = requests.post(AUTHORS_ENDPOINT, json=NEW_AUTHOR_DATA)
    assert response.status_code in [200, 201]
    
    data = response.json()
    assert data["id"] == NEW_AUTHOR_DATA["id"]
    assert data["idBook"] == NEW_AUTHOR_DATA["idBook"]
    assert data["firstName"] == NEW_AUTHOR_DATA["firstName"]
    assert data["lastName"] == NEW_AUTHOR_DATA["lastName"]
