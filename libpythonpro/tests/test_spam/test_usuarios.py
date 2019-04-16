from PythonPro.libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Wagner', email='wagherculano@hotmailcom')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Wagner', email='wagherculano@hotmailcom'),
                Usuario(nome='Danielle', email='danielle@danielle.com.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
