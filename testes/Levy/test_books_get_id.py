import requests
from config import BOOKS_ENDPOINT

def test_tc11_list_all_books_success():
    """TC11: Listar todos os livros (GET /Books)"""
    response = requests.get(BOOKS_ENDPOINT)
    
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list), "A resposta deve ser uma lista."
    assert len(data) > 0, "A lista de livros não pode estar vazia."
