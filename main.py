from api import Apipol
if __name__ == '__main__':
    # buscar_deputados()
    despesas = Apipol.buscar_deputados_id_despesas(
        "220704", {'ano': '2023', 'mes': '03'})
    total = 0
    for cont, desp in enumerate(despesas):
        for item in desp:
            if item == 'ano':
                print(f'Despesa Nro: {desp["codDocumento"]}')
            print(f'    {item}:{desp[item]}')
            if item == 'valorDocumento':
                total += desp[item]
    print(f'\nO total das notas é: {total}')
