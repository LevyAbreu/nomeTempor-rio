import requests


class TestGetActivities:
    BASE_URL = "http://localhost:5077/api/v1"  # ajuste a porta da sua API

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
        requests.post(criar_url, json=payload)

        # Agora realizar o GET pelo ID
        url = f"{self.BASE_URL}/Activities/1"
        resp = requests.get(url)

        assert resp.status_code == 200
        dados = resp.json()
        assert dados["id"] == 1
        assert dados["title"] == "Teste busca"
