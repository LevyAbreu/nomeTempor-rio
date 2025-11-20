import requests


class TestGetActivities:
    BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"  # ajuste a porta da sua API

    # TC01 - Listar todas as atividades
    def test_tc01_listar_todas_atividades(self):
        url = f"{self.BASE_URL}/Activities"
        resp = requests.get(url)

        assert resp.status_code == 200
        dados = resp.json()
        assert isinstance(dados, list)

    # TC02 - Buscar atividade por ID
    def test_tc02_buscar_atividade_por_id(self):
        # Primeiro garantir que exista uma atividade com ID = 1
        criar_url = f"{self.BASE_URL}/Activities"
        payload = {
            "id": 1,
            "title": "Teste busca",
            "isCompleted": False
        }
        post_resp = requests.post(criar_url, json=payload)
        assert post_resp.status_code in (200, 201)
        created = post_resp.json()
        created_id = created.get("id", 1)

        url = f"{self.BASE_URL}/Activities/{created_id}"
        resp = requests.get(url)

        assert resp.status_code == 200
        dados = resp.json()
        assert dados["id"] == created_id
        # API may not persist the posted title; ensure the returned object has a title string
        assert isinstance(dados.get("title"), str)
