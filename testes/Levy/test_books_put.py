import requests
import pytest
from config import BOOKS_ENDPOINT

BOOK_ID_TO_UPDATE = 1 
UPDATED_TITLE = "Título Atualizado por Manus"

def test_tc14_update_book_success():
    """TC14: Atualizar livro (PUT /Books/{id})"""
    url = f"{BOOKS_ENDPOINT}/{BOOK_ID_TO_UPDATE}"
    
    get_response = requests.get(url)
    assert get_response.status_code == 200
    book_data = get_response.json()
    
    book_data["title"] = UPDATED_TITLE
    
    put_response = requests.put(url, json=book_data)
    
    assert put_response.status_code == 200
    
    updated_data = put_response.json()
    assert updated_data["title"] == UPDATED_TITLE