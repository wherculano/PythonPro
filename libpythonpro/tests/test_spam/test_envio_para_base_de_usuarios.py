from unittest.mock import Mock
import pytest
from PythonPro.libpythonpro.spam.main import EnviadorDeSpam
from PythonPro.libpythonpro.spam.modelos import Usuario


#  Testar quantos spams foram enviados
@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Wagner', email='wagherculano@hotmailcom'),
            Usuario(nome='Danielle', email='danielle@danielle.com.br')
        ],
        [
            Usuario(nome='Wagner', email='wagherculano@hotmailcom')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'wagherculano@hotmail.com',
        'Teste Spam',
        'Testando envio de spams'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Wagner', email='wagherculano@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'danielle@danielle.com.br',
        'Teste Spam',
        'Testando envio de spams'
    )
    enviador.enviar.assert_called_once_with(
        'danielle@danielle.com.br',
        'wagherculano@hotmail.com',
        'Teste Spam',
        'Testando envio de spams'
    )
