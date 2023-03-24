import requests
import json


def buscar_deputados_id(id):
    request = requests.get(
        f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id}")
    todo = json.loads(request.content)
    return (todo["dados"] if "dados" in todo else None)


data = buscar_deputados_id(3652541)

print(data)
