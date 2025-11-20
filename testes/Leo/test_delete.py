import requests
import pytest
from config import COVER_PHOTOS_ENDPOINT

COVER_PHOTO_TO_DELETE = {
    "id": 999,
    "idBook": 1,
    "url": "https://example.com/cover_to_delete.jpg"
}

@pytest.fixture(scope="module")
def setup_cover_photo_for_deletion():
    """Cria uma CoverPhoto antes dos testes e tenta deletá-la."""
    post_response = requests.post(COVER_PHOTOS_ENDPOINT, json=COVER_PHOTO_TO_DELETE)
    assert post_response.status_code in [200, 201]
    
    yield COVER_PHOTO_TO_DELETE["id"]
    
def test_tc26_delete_cover_photo_success(setup_cover_photo_for_deletion):
    """TC26: Deletar CoverPhoto por ID (DELETE /CoverPhotos/{id})"""
    cover_photo_id = setup_cover_photo_for_deletion
    url = f"{COVER_PHOTOS_ENDPOINT}/{cover_photo_id}"
    
    delete_response = requests.delete(url)
    
    assert delete_response.status_code == 200
    
    get_response = requests.get(url)
    assert get_response.status_code == 404
