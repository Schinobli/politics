from api import Apipol

dados = Apipol.buscar_deputados()
for x in dados:
    print(x)
