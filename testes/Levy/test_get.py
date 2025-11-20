import requests
import pytest
from config import BOOKS_ENDPOINT

EXPECTED_SCHEMA = {
    "id": int,
    "title": str,
    "description": str,
    "pageCount": int,
    "excerpt": str,
    "publishDate": str
}

@pytest.mark.parametrize("book_id", [1, 5, 10])
def test_tc12_get_book_by_id_success(book_id):
    """TC12: Buscar livro por ID (GET /Books/{id})"""
    url = f"{BOOKS_ENDPOINT}/{book_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id
    assert "title" in data
    assert "description" in data

def test_tc11_list_all_books_success():
    """TC11: Listar todos os livros (GET /Books)"""
    response = requests.get(BOOKS_ENDPOINT)
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

@pytest.mark.parametrize("book_id", [1, 5, 10])
def test_tc15_validate_data_types(book_id):
    """TC15: Validar tipos de dados (GET /Books/{id})"""
    url = f"{BOOKS_ENDPOINT}/{book_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()
    
    for key, expected_type in EXPECTED_SCHEMA.items():
        assert key in data, f"Campo '{key}' não encontrado na resposta."
        assert isinstance(data[key], expected_type), f"Tipo incorreto para o campo '{key}'. Esperado: {expected_type}, Recebido: {type(data[key])}"
