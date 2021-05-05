from flask import Flask, jsonify, request
from main import query,execute,insert,select,delete,update
from serializers import genero_from_db, genero_from_web
from models import get_genero, insert_genero
from validacao import valida_genero

app = Flask(__name__)


@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        insert_genero(**genero)
        genero_criado = get_genero(genero["nome"])
        return jsonify(genero_from_db(genero_criado))
    else:
        return jsonify("erro", "genero inválido")


def get_generos():
    nome = request.args.get("nome")
    return jsonify(query("select * from generos where nome = %s",(nome)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
