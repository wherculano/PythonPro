from PythonPro.libpythonpro.spam.db import Conexao
from PythonPro.libpythonpro.spam.modelos import Usuario


def test_salvar_usuario():
    conexao = Conexao()  # gerencia a autenticacao com o BD (lgin e senha)
    sessao = conexao.gerar_sessao()  # efetuar alteracoe no BD (CRUD)
    usuario = Usuario(nome='Wagner')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuarios():
    conexao = Conexao()  # gerencia a autenticacao com o BD (lgin e senha)
    sessao = conexao.gerar_sessao()  # efetuar alteracoe no BD (CRUD)
    usuarios = [Usuario(nome='Wagner'), Usuario(nome='Danielle')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
