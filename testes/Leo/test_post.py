import requests
import pytest
from config import COVER_PHOTOS_ENDPOINT

NEW_COVER_PHOTO_DATA = {
    "id": 101,
    "idBook": 1,
    "url": "https://example.com/cover101.jpg"
}

def test_tc23_create_new_cover_photo_success():
    """TC23: Criar nova CoverPhoto (POST /CoverPhotos)"""
    response = requests.post(COVER_PHOTOS_ENDPOINT, json=NEW_COVER_PHOTO_DATA)
    
    assert response.status_code in [200, 201]
    
    data = response.json()
    assert data["id"] == NEW_COVER_PHOTO_DATA["id"]
    assert data["idBook"] == NEW_COVER_PHOTO_DATA["idBook"]
    assert data["url"] == NEW_COVER_PHOTO_DATA["url"]
