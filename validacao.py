import datetime

from models import get_genero


def valida_genero(nome):
    if len(nome) == 0:
        return False
    return True


def valida_diretores(nome_completo):
    if len(nome_completo) == 0:
        return False
    return True


def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True


def valida_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    if len(titulo) == 0:
        return False
    if len(ano) == 0:
        return False
    if len(classificacao) == 0:
        return False
    if len(preco) == 0:
        return False
    if diretores_id == 0:
        return False
    if str(generos_id) == 0:
        return False
    return True


def valida_locacao(data_inicio, data_fim, filmes_id, usuarios_id):
    if datetime.date(data_inicio) > datetime.date(data_fim):
        return False
    if len(filmes_id) == 0:
        return False
    if len(usuarios_id) == 0:
        return False
    return True


def valida_pagamento(tipo, status, codigo_pagamento, valor, data, locacao_id):
    if len(tipo) == 0:
        return False
    if len(status) == 0:
        return False
    if len(codigo_pagamento) == 0:
        return False
    if len(valor) == 0:
        return False
    if len(data) == 0:
        return False
    if locacao_id == 0:
        return False
