import pytest
from PythonPro.libpythonpro.spam.db import Conexao
from PythonPro.libpythonpro.spam.modelos import Usuario


#  Fixtures para Setup do BD
@pytest.fixture
def conexao():
    conexao_obj = Conexao()  # gerencia a autenticacao com o BD (login e senha)
    yield conexao_obj  # retorna o valor que será injetado nos testes
    conexao_obj.fechar()  # Tear Down


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()  # efetuar alteracoe no BD (CRUD)
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Wagner')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Wagner'), Usuario(nome='Danielle')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
