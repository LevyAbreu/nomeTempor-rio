import requests


class TestDeleteActivities:
    BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"

    def test_tc05_deletar_atividade(self):
        url = f"{self.BASE_URL}/Activities/1"
        resp = requests.delete(url)

        assert resp.status_code in (200, 204)
