import pytest

from PythonPro.libpythonpro.spam.enviador_de_email import Enviador
from PythonPro.libpythonpro.spam.main import EnviadorDeSpam

#  Testar quantos spams foram enviados
from PythonPro.libpythonpro.spam.modelos import Usuario


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'wagherculano@hotmail.com',
        'Teste Spam',
        'Testando envio de spams'
    )
    assert len(usuarios) == enviador.qde_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qde_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, mensagem):
        self.parametros_de_envio = (remetente, destinatario, assunto, mensagem)
        self.qde_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Wagner', email='wagherculano@hotmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'danielle@danielle.com.br',
        'Teste Spam',
        'Testando envio de spams'
    )
    assert enviador.parametros_de_envio == (
        'danielle@danielle.com.br',
        'wagherculano@hotmail.com',
        'Teste Spam',
        'Testando envio de spams'
    )
