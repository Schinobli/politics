import requests
import json


def filtros(args):
    dados = ''.join([f'{x}={args[x]}&' for x in args])[:-1]
    return dados


class Apipol:
    def buscar_deputados_id(id):
        request = requests.get(
            f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id}")
        todo = json.loads(request.content)
        return (todo['dados'])

    def buscar_deputados_id_profissoes(id):
        request = requests.get(
            f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id}/profissoes")
        todo = json.loads(request.content)
        return (todo['dados'])

    def buscar_deputados():
        request = requests.get(
            f"https://dadosabertos.camara.leg.br/api/v2/deputados")
        todo = json.loads(request.content)
        return (todo['dados'])

    def buscar_deputados_id_despesas(id, filtro=False):
        if filtro:
            request = requests.get(
                f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id}/despesas?{filtros(filtro)}")

        else:
            request = requests.get(
                f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id}/despesas")

        todo = json.loads(request.content)
        return (todo['dados'])
