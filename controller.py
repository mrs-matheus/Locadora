from flask import Flask, jsonify, request
from cmd_bd import select, select_like, execute, query
from datetime import datetime, timedelta
from random import randint, random

##imports de usuarios:
from serializers import usuario_from_web, usuario_from_db, nome_usuario_from_web
from models import insert_usuario, get_usuario, update_usuario, delete_usuario, select_usuario
from validacao import valida_usuario

## imports dos generos:
from serializers import genero_from_db, genero_from_web
from models import insert_genero, get_genero, update_genero, delete_genero
from validacao import valida_genero

## imports dos diretores
from serializers import diretores_from_db, diretores_from_web
from models import insert_diretor, get_diretor, update_diretor, delete_diretor
from validacao import valida_diretores

## imports dos filmes
from serializers import filmes_from_web, filmes_from_db
from models import get_filme, insert_filme, update_filme, delete_filme
from validacao import valida_filme

## imports das locacoes
from serializers import locacoes_from_db, locacoes_from_web
from models import insert_locacao, get_locacao, update_locacao, delete_locacao
from validacao import valida_locacao

# imports dos pagamentos
from serializers import pagamento_from_db, pagamento_from_web
from models import insert_pagamento, get_pagamento, update_pagamento, delete_pagamento
from validacao import valida_pagamento

app = Flask(__name__)


@app.route("/diretores", methods=["POST"])
def inserir_diretores():
    diretor = diretores_from_web(**request.json)
    if valida_diretores(**diretor):
        insert_diretor(**diretor)
        diretor_criado = get_diretor(diretor["nome_completo"])
        return jsonify(diretores_from_db(diretor_criado))
    else:
        return jsonify("erro", "diretor inválido")


@app.route("/diretores", methods=["GET"])
def get_diretores():
    return jsonify(select("diretores"))


@app.route("/diretores/<int:id>", methods=["PUT", "PATCH"])
def update_diretores(id):
    diretor = diretores_from_web(**request.json)
    if valida_diretores(**diretor):
        update_diretor(id, **diretor)
        diretor_alterado = get_diretor(id)
        return jsonify(diretores_from_db(diretor_alterado))


@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretores(id):
    try:
        delete_diretor(id)
        return "", 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})


@app.route("/generos", methods=["POST"])
def inserir_generos():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        id_genero = insert_genero(**genero)
        genero_criado = get_genero(genero[id_genero])
        return jsonify(genero_from_db(genero_criado))
    else:
        return jsonify("erro", "genero inválido")


@app.route("/generos", methods=["GET"])
def buscar_genero():
    return jsonify(select("generos"))


@app.route("/generos/<int:id>", methods=["PUT", "PATCH"])
def update_genero(id):
    genero = diretores_from_web(**request.json)
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_alterado = get_genero(id)
        return jsonify(diretores_from_db(genero_alterado))


@app.route("/generos/<int:id>", methods=["DELETE"])
def delete_genero(id):
    try:
        delete_genero(id)
        return None, 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})


@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuario(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)


@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return "", 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})


@app.route("/filmes", methods=["POST"])
def inserir_filme():
    filmes = filmes_from_web(**request.json)
    if valida_filme(**filmes):
        id_filme = insert_filme(**filmes)
        filme_criado = get_filme(id_filme)
        return jsonify(filmes_from_db(filme_criado))
    else:
        return jsonify({"erro": "filme invalido"})


@app.route("/filmes", methods=["GET"])
def buscar_filme():
    return jsonify(select("filmes"))


@app.route("/filmes/<int:id>", methods=["PUT", "PATCH"])
def alterar_filme(id):
    filme = filmes_from_web(**request.json)
    if valida_filme(**filme):
        update_filme(id, **filme)
        filme_alterado = get_filme(id)
        return jsonify(filmes_from_db(filme_alterado))
    else:
        return jsonify({"erro": "filme nao foi alterado"})


@app.route("/filmes/<int:id>", methods=["DELETE"])
def deletar_filme(id):
    try:
        delete_filme(id)
        return "", 204
    except:
        return jsonify({"erro": "Filme não deletado"})


@app.route("/locacoes", methods=["POST"])
def inserir_locacao():
    locacao = locacoes_from_web(**request.json)
    if valida_pagamento(**locacao):
        id_locacao = insert_locacao(locacao)
        locacao_cadastrada = get_pagamento(id_locacao)
        return jsonify(locacoes_from_db(locacao_cadastrada))
    else:
        return jsonify({"erro": "locacao não cadastrado"})


@app.route("/locacoes", methods=["GET"])
def buscar_locacao():
    return jsonify(select("locacoes"))


@app.route("/locacoes/<int:id>", methods=["PUT,PATCH"])
def alterar_locacao(id):
    locacao = locacoes_from_web(**request.json)
    if valida_locacao(**locacao):
        update_locacao(id, **locacao)
        locacao_alterada = get_locacao(id)
        return jsonify(locacoes_from_db(locacao_alterada))
    else:
        return jsonify({"erro": "Locação de filmes não foi alterada"})


@app.route("/locacoes/<int:id>", methods=["DELETE"])
def deletar_locacao(id):
    try:
        delete_locacao(id)
        return "", 204
    except:
        return jsonify("erro", "Locação não deletada")


@app.route("/pagamento", methods=["POST"])
def inserir_pagamento():
    paga = pagamento_from_web(**request.json)
    if valida_pagamento(**paga):
        id_pagamento = insert_pagamento(paga)
        pagamento_cadastrado = get_pagamento(id_pagamento)
        return jsonify(pagamento_from_db(pagamento_cadastrado))
    else:
        return jsonify({"erro": "pagamento não cadastrado"})


@app.route("/pagamento/<int:id>", methods=["GET"])
def buscar_pagamento(id):
    return jsonify(select_like("pagamento", "id", id))


@app.route("/pagamento/<int:id>", methods=["PUT.PATCH"])
def alterar_pagamento(id):
    pag = pagamento_from_web(**request.json)
    if valida_pagamento(**pag):
        update_pagamento(id, **pag)
        pag_alterado = get_pagamento(id)
        return jsonify(pagamento_from_db(pag_alterado))
    else:
        return jsonify({"erro": "Pagamento não foi atualizado"})


@app.route("/pagamento/<int:id>")
def deletar_pagamento(id):
    try:
        delete_pagamento(id)
        return "", 204
    except:
        return jsonify({"erro": "não foi possivel apagar o pagamento"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
