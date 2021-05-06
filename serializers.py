def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else ""
    }


def genero_from_db(*args):
    return {
        "nome": args[0]
    }


def diretores_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }


def diretores_from_db(*args):
    return {
        "nome_completo": args[0]
    }
