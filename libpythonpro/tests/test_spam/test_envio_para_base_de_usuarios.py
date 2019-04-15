from PythonPro.libpythonpro.spam.enviador_de_email import Enviador
from PythonPro.libpythonpro.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'wagherculano@hotmail.com',
        'Teste Spam',
        'Testando envio de spams'
    )
