import requests


class TestPostActivities:
    BASE_URL = "http://localhost:5077/api/v1"

    def test_tc03_criar_nova_atividade(self):
        url = f"{self.BASE_URL}/Activities"
        payload = {
            "id": 1,
            "title": "Estudar API",
            "isCompleted": False
        }

        resp = requests.post(url, json=payload)

        assert resp.status_code in (200, 201)
        dados = resp.json()
        assert dados.get("title") == "Estudar API"
