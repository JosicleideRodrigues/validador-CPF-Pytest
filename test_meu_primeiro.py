import re

# Item 2: Função que valida o formato do CPF
def validar_cpf_formato(cpf: str) -> bool:
    if cpf is None:
        return False
    # Define o padrão: 3 números . 3 números . 3 números - 2 números
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, str(cpf)))

# Item 3: Testes para os diferentes cenários
def test_cpf_valido():
    assert validar_cpf_formato("123.456.789-00") is True

def test_cpf_sem_pontuacao():
    assert validar_cpf_formato("12345678900") is False

def test_cpf_com_letras():
    assert validar_cpf_formato("123.abc.789-00") is False

def test_string_vazia():
    assert validar_cpf_formato("") is False

def test_cpf_none():
    assert validar_cpf_formato(None) is False