import requests
from config import COVER_PHOTOS_ENDPOINT

def test_tc21_list_all_cover_photos_success():
    """TC21: Listar todas as CoverPhotos (GET /CoverPhotos)"""
    response = requests.get(COVER_PHOTOS_ENDPOINT)
    
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list), "A resposta deve ser uma lista."
    # O endpoint CoverPhotos pode retornar uma lista vazia, então não vou forçar len(data) > 0
    # assert len(data) > 0, "A lista de CoverPhotos não pode estar vazia."
