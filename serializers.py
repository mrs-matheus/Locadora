from cmd_bd import query, select, execute


def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else ""
    }


def genero_from_db(nome):
    return {
        "nome": nome["nome"]
    }


def diretores_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }


def diretores_from_db(nome_completo):
    return {
        "nome_completo": nome_completo["nome_completo"]
    }


def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""

    }


def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else "",
    }


def usuario_from_db(usuario):
    return {
        "id": usuario["id"],
        "nome_completo": usuario["nome_completo"],
        "CPF": usuario["CPF"]
    }


def nome_usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""


def filmes_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": kwargs["preco"] if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else ""
    }


def filmes_from_db(filmes):
    return {
        "id": filmes["id"],
        "titulo": filmes["titulo"],
        "ano": filmes["ano"],
        "classificacao": filmes["classificacao"],
        "preco": str(filmes["preco"]),
        "diretores_id": filmes["diretores_id"],
        "generos_id": filmes["generos_id"]
    }


def locacoes_from_web(**kwargs):
    return {
        "data_inicio": kwargs["data_inicio"] if "data_inicio" in kwargs else "",
        "data_fim": kwargs["data_fim"] if "data_fim" in kwargs else "",
        "filmes_id": kwargs["filmes_id"] if "filmes_id" in kwargs else "",
        "usuarios_id": kwargs["usuarios_id"] if "usuaiors_is" in kwargs else "",
    }


def locacoes_from_db(locacoes):
    return {
        "data_inicio": locacoes["data_inicio"],
        "data_fim": locacoes["data_fim"],
        "filmes_id": locacoes["filmes_id"],
        "usuarios_id": locacoes["usuarios_id"]
    }
