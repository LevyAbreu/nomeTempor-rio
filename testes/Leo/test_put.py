import requests
import pytest
from config import COVER_PHOTOS_ENDPOINT

COVER_PHOTO_ID_TO_UPDATE = 1 
UPDATED_URL = "https://example.com/updated_cover.jpg"

def test_tc24_update_cover_photo_success():
    """TC24: Atualizar CoverPhoto (PUT /CoverPhotos/{id})"""
    url = f"{COVER_PHOTOS_ENDPOINT}/{COVER_PHOTO_ID_TO_UPDATE}"
    
    get_response = requests.get(url)
    assert get_response.status_code == 200
    cover_photo_data = get_response.json()
    
    cover_photo_data["url"] = UPDATED_URL
    
    put_response = requests.put(url, json=cover_photo_data)
    
    assert put_response.status_code == 200
    
    updated_data = put_response.json()
    assert updated_data["url"] == UPDATED_URL
