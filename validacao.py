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
