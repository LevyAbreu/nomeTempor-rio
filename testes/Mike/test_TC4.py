import requests


class TestPutActivities:
    BASE_URL = "http://localhost:5077/api/v1"

    def test_tc04_atualizar_atividade(self):
        url = f"{self.BASE_URL}/Activities/1"
        payload = {
            "id": 1,
            "title": "Atualizado",
            "isCompleted": True
        }

        resp = requests.put(url, json=payload)

        assert resp.status_code == 200
        dados = resp.json()
        assert dados.get("isCompleted") == True
