import requests
from config import COVER_PHOTOS_ENDPOINT
import pytest

@pytest.mark.parametrize("book_id", [1, 5, 10])
def test_tc27_get_cover_photos_by_book_id_success(book_id):
    """TC27: Buscar CoverPhotos por ID do Livro (GET /CoverPhotos/books/covers/{idBook})"""
    url = f"{COVER_PHOTOS_ENDPOINT}/books/covers/{book_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list), "A resposta deve ser uma lista."
    # O endpoint pode retornar uma lista vazia, então não vou forçar len(data) > 0
    # assert len(data) > 0, "A lista de CoverPhotos não pode estar vazia."
    
    # Se houver dados, verifica se todos pertencem ao idBook correto
    if data:
        for item in data:
            assert item["idBook"] == book_id
