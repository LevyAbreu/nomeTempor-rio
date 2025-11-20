import requests


class TestPutActivities:
    BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"

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
        assert dados.get("title") == payload["title"]
        assert isinstance(dados.get("completed"), bool) or isinstance(dados.get("isCompleted"), bool)
