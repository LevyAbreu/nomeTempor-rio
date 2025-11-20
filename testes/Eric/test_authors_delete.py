import requests
import pytest
from config import AUTHORS_ENDPOINT

AUTHOR_TO_DELETE = {
    "id": 999,
    "idBook": 1,
    "firstName": "Autor",
    "lastName": "Para Deletar"
}

@pytest.fixture(scope="module")
def setup_author_for_deletion():
    """Cria um Author antes dos testes e tenta deletá-lo."""
    post_response = requests.post(AUTHORS_ENDPOINT, json=AUTHOR_TO_DELETE)
    assert post_response.status_code in [200, 201]
    
    yield AUTHOR_TO_DELETE["id"]
    
def test_tc36_delete_author_success(setup_author_for_deletion):
    """TC36: Deletar Author por ID (DELETE /Authors/{id})"""
    author_id = setup_author_for_deletion
    url = f"{AUTHORS_ENDPOINT}/{author_id}"
    
    delete_response = requests.delete(url)
    
    assert delete_response.status_code == 200
    
    get_response = requests.get(url)
    assert get_response.status_code == 404
