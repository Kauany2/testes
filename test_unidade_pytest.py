import pytest

from livro import Livro, Exemplar
from exceptions import TipoIncorretoException, AnoInvalidoException,QuantidadeInvalidaException

def test_criar_novo_livro():
    novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)

    assert novo_livro.titulo == "The Art of Software Testing"
    assert novo_livro.autores == ["John Glenford Myers", "Corey Sandler", "Tom Badget"]
    assert novo_livro.ano_publicacao == 1976

def livro_exemplo():
    return Livro("Título do Livro", ["Autor 1", "Autor 2"], 2020)

def test_criar_exemplar_com_sucesso(livro_exemplo):
    exemplar = Exemplar(livro_exemplo, 5, 1, 2022, "Editora")
    assert exemplar.livro == livro_exemplo
    assert exemplar.quantidade == 5
    assert exemplar.edicao == 1
    assert exemplar.ano == 2022
    assert exemplar.editora == "Editora"

def test_criar_exemplar_com_tipo_incorreto():
    with pytest.raises(TipoIncorretoException):
        exemplar = Exemplar(1, 5, 1, 2022, "Editora")
        exemplar.livro = 2

def test_ano_invalido(livro_exemplo):
    with pytest.raises(AnoInvalidoException):
        exemplar = Exemplar(livro_exemplo, 5, 1, 2019, "Editora")

def test_quantidade_invalida(livro_exemplo):
    with pytest.raises(QuantidadeInvalidaException):
        exemplar = Exemplar(livro_exemplo, -5, 1, 2022, "Editora")

def test_adicionar_exemplares(livro_exemplo):
    exemplar = Exemplar(livro_exemplo, 5, 1, 2022, "Editora")
    exemplar.adicionar_exemplares(3)
    assert exemplar.quantidade == 8

def test_remover_exemplares(livro_exemplo):
    exemplar = Exemplar(livro_exemplo, 5, 1, 2022, "Editora")
    exemplar.remover_exemplares(2)
    assert exemplar.quantidade == 3


def test_alterar_titulo_do_livro(livro_exemplo):
    livro_exemplo.titulo = "Novo Título"
    assert livro_exemplo.titulo == "Novo Título"

def test_alterar_autores_do_livro(livro_exemplo):
    livro_exemplo.autores = ["Novo Autor 1", "Novo Autor 2"]
    assert livro_exemplo.autores == ["Novo Autor 1", "Novo Autor 2"]

def test_alterar_ano_publicacao_do_livro(livro_exemplo):
    livro_exemplo.ano_publicacao = 2021
    assert livro_exemplo.ano_publicacao == 2021

def test_adicionar_exemplares_com_sucesso(livro_exemplo):
    exemplar = Exemplar(livro_exemplo, 5, 1, 2022, "Editora")
    exemplar.adicionar_exemplares(3)
    assert exemplar.quantidade == 8

def test_adicionar_exemplares_com_quantidade_invalida(livro_exemplo):
    exemplar = Exemplar(livro_exemplo, 5, 1, 2022, "Editora")
    with pytest.raises(QuantidadeInvalidaException):
        exemplar.adicionar_exemplares(-2)

def test_remover_exemplares_com_sucesso(livro_exemplo):
    exemplar = Exemplar(livro_exemplo, 5, 1, 2022, "Editora")
    exemplar.remover_exemplares(2)
    assert exemplar.quantidade == 3

def test_remover_exemplares_com_quantidade_invalida(livro_exemplo):
    exemplar = Exemplar(livro_exemplo, 5, 1, 2022, "Editora")
    with pytest.raises(QuantidadeInvalidaException):
        exemplar.remover_exemplares(-2)
