import requests
from config import AUTHORS_ENDPOINT

def test_tc31_list_all_authors_success():
    """TC31: Listar todos os Authors (GET /Authors)"""
    response = requests.get(AUTHORS_ENDPOINT)
    
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list), "A resposta deve ser uma lista."
