import requests
import pytest
from config import COVER_PHOTOS_ENDPOINT

EXPECTED_SCHEMA = {
    "id": int,
    "idBook": int,
    "url": str
}

@pytest.mark.parametrize("cover_photo_id", [1, 5, 10])
def test_tc22_get_cover_photo_by_id_success(cover_photo_id):
    """TC22: Buscar CoverPhoto por ID (GET /CoverPhotos/{id})"""
    url = f"{COVER_PHOTOS_ENDPOINT}/{cover_photo_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == cover_photo_id
    assert "idBook" in data
    assert "url" in data

@pytest.mark.parametrize("cover_photo_id", [1, 5, 10])
def test_tc25_validate_data_types(cover_photo_id):
    """TC25: Validar tipos de dados do retorno (GET /CoverPhotos/{id})"""
    url = f"{COVER_PHOTOS_ENDPOINT}/{cover_photo_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    for key, expected_type in EXPECTED_SCHEMA.items():
        assert key in data, f"Campo '{key}' não encontrado."
        assert isinstance(data[key], expected_type), (
            f"Campo '{key}' deveria ser {expected_type}, "
            f"mas veio {type(data[key])}."
        )
