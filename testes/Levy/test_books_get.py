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

@pytest.mark.parametrize("book_id", [1, 5, 10])
def test_tc15_validate_data_types(book_id):
    """TC15: Validar tipos de dados do retorno (GET /Books/{id})"""
    url = f"{BOOKS_ENDPOINT}/{book_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    for key, expected_type in EXPECTED_SCHEMA.items():
        assert key in data, f"Campo '{key}' não encontrado."
        assert isinstance(data[key], expected_type), (
            f"Campo '{key}' deveria ser {expected_type}, "
            f"mas veio {type(data[key])}."
        )
