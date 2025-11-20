import requests
import pytest
from config import BOOKS_ENDPOINT

BOOK_TO_DELETE = {
    "id": 999,
    "title": "Livro para Deletar",
    "description": "Este livro será deletado.",
    "pageCount": 100,
    "excerpt": "Trecho para deleção.",
    "publishDate": "2025-11-20T00:00:00Z"
}

@pytest.fixture(scope="module")
def setup_book_for_deletion():
    """Cria um livro antes dos testes e tenta deletá-lo."""
    post_response = requests.post(BOOKS_ENDPOINT, json=BOOK_TO_DELETE)
    assert post_response.status_code == 200
    
    yield BOOK_TO_DELETE["id"]
    
def test_tc16_delete_book_success(setup_book_for_deletion):
    """TC16: Deletar livro por ID (DELETE /Books/{id})"""
    book_id = setup_book_for_deletion
    url = f"{BOOKS_ENDPOINT}/{book_id}"
    
    delete_response = requests.delete(url)
    
    assert delete_response.status_code == 200
    
    pass
