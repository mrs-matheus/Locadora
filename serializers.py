def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else ""
    }


def genero_from_db(*args):
    return {
        "nome": args["nome"]
    }


def diretores_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }


def diretores_from_db(*args):
    return {
        "nome_completo": args["nome_completo"]
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
