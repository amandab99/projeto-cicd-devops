from mensagem import saudacao

def test_saudacao_normal():
    assert saudacao("Amanda") == "Olá, Amanda!"

def test_saudacao_vazia():
    assert saudacao("") == "Olá, !"

def test_saudacao_minuscula():
    assert saudacao("amanda") == "Olá, amanda!"

def test_saudacao_com_espaco():
    assert saudacao(" Amanda ") == "Olá,  Amanda !"

def test_saudacao_numeros():
    assert saudacao("123") == "Olá, 123!"
