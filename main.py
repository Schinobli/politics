from flask import Flask, render_template, send_from_directory, request
from api import Apipol

app = Flask(__name__, static_folder='static', template_folder='templates')

# Rota para servir arquivos estáticos


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# Rota para a página inicial


@app.route('/')
def homepage():
    deputados = Apipol.buscar_deputados(None)
    idx = 0
    bef = 0
    aft = 1
    idx_f = 12
    return render_template("homepage.html", idx=idx, idx_f=idx_f, len=len(deputados), bef=bef, aft=aft, deputados=deputados)


@app.route('/pagina/<pag>')
def homepage2(pag):
    deputados = Apipol.buscar_deputados(None)

    try:
        pag = int(pag)
        bef = pag-1
        aft = pag+1
        idx = 12*pag
        idx_f = idx+12
        if not deputados:
            raise Exception
        if pag/12+1 > 12:
            raise Exception
    except:
        return render_template("home404.html")

    return render_template("homepage.html", idx=idx, idx_f=idx_f, len=len(deputados), bef=bef, aft=aft, deputados=deputados)


@app.route('/deputado/<id>')
def user(id):
    data = Apipol.buscar_deputados_id(id)
    if not data:
        return render_template("home404.html")
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


@app.route('/search')
def search():
    search_term = request.args.get('search_term')
    search_by = request.args.get('search_by')
    deputados = Apipol.buscar_deputados({search_by: search_term})
    if not deputados:
        return render_template("home404.html")

    idx = 0
    bef = 0
    aft = 1
    idx_f = len(deputados) if len(deputados) <= 12 else 12

    return render_template("homepage.html", idx=idx, idx_f=idx_f, len=len(deputados), bef=bef, aft=aft, deputados=deputados)


if __name__ == "__main__":
    app.run(debug=True)
