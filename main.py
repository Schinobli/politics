from flask import Flask, render_template
from api import Apipol

app = Flask(__name__, static_folder='')

# route -> caminho
# função -> o que quer exibir na página


@app.route('/')
def homepage():
    deputados = Apipol.buscar_deputados()
    idx = 0
    bef = 0
    aft = 1
    idx_f = 12
    return render_template("homepage.html", idx=idx, idx_f=idx_f, len=len(deputados), bef=bef, aft=aft, deputados=deputados)


@app.route('/pagina/<pag>')
def homepage2(pag):
    deputados = Apipol.buscar_deputados()

    try:
        pag = int(pag)
        bef = pag-1
        aft = pag+1
        idx = 12*pag
        idx_f = idx+12
    except:
        idx = 0
        bef = 0
        aft = 1
        idx_f = 12
    return render_template("homepage.html", idx=idx, idx_f=idx_f, len=len(deputados), bef=bef, aft=aft, deputados=deputados)


@app.route('/deputado/<id>')
def user(id):
    data = Apipol.buscar_deputados_id(id)
    nomecivil = data["nomeCivil"]
    foto = data["ultimoStatus"]["urlFoto"]
    nome = data["ultimoStatus"]["nome"]
    partido = data["ultimoStatus"]["siglaPartido"]
    uf = data["ultimoStatus"]["siglaUf"]
    situacao = data["ultimoStatus"]["situacao"]
    cpf = data["cpf"]
    sexo = data["sexo"]
    data_nasc = data["dataNascimento"]
    email = data["ultimoStatus"]["gabinete"]["email"]
    site = data["urlWebsite"]
    redesocial = data["redeSocial"]

    despesas = Apipol.buscar_deputados_id_despesas(id)
    total = round(sum(x["valorDocumento"] for x in despesas), 2)
    profissoes = Apipol.buscar_deputados_id_profissoes(id)

    return render_template("perfil.html", id=id, situacao=situacao, cpf=cpf,
                           data_nasc=data_nasc, nome=nome, foto=foto,
                           nomecivil=nomecivil, partido=partido,
                           uf=uf, email=email, sexo=sexo, site=site,
                           redesocial=redesocial, lendes=len(despesas),
                           despesas=despesas, total=total,
                           lenpro=len(profissoes), profissoes=profissoes)


if __name__ == "__main__":
    app.run(debug=True)
