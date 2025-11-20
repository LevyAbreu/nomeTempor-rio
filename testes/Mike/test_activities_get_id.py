import requests


class TestGetActivities:
    BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"

    def test_tc01_listar_todas_atividades(self):
        url = f"{self.BASE_URL}/Activities"
        resp = requests.get(url)

        assert resp.status_code == 200
        assert isinstance(resp.json(), list)

    def test_tc02_buscar_atividade_por_id(self):
        url = f"{self.BASE_URL}/Activities/1"
        resp = requests.get(url)

        assert resp.status_code == 200
        dados = resp.json()
        assert dados["id"] == 1
