import requests
from config import AUTHORS_ENDPOINT
import pytest

@pytest.mark.parametrize("book_id", [1, 5, 10])
def test_tc37_get_authors_by_book_id_success(book_id):
    """TC37: Buscar Authors por ID do Livro (GET /Authors/authors/books/{idBook})"""
    url = f"{AUTHORS_ENDPOINT}/authors/books/{book_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list), "A resposta deve ser uma lista."
    if data:
        for item in data:
            assert item["idBook"] == book_id
