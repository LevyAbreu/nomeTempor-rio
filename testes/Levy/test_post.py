import requests
import pytest
from config import BOOKS_ENDPOINT

NEW_BOOK_DATA = {
    "id": 201,
    "title": "Livro de Teste Manus",
    "description": "Descrição do Livro de Teste Manus",
    "pageCount": 500,
    "excerpt": "Um trecho do livro de teste.",
    "publishDate": "2025-11-20T00:00:00Z"
}

def test_tc13_create_new_book_success():
    """TC13: Criar novo livro (POST /Books)"""
    response = requests.post(BOOKS_ENDPOINT, json=NEW_BOOK_DATA)
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == NEW_BOOK_DATA["id"]
    assert data["title"] == NEW_BOOK_DATA["title"]