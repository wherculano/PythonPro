import pytest

from PythonPro.libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['wagner@herculano.com.br', 'foo@bar.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,  # remetente
        'herculano@wagner.com.br',  # destinatario
        'Teste Spam',  # assunto
        'Testando enviador de spam')  # mensagem
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['wagner', '', 'foo.com.br']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,  # remetente
            'herculano@wagner.com.br',  # destinatario
            'Teste Spam',  # assunto
            'Testando enviador de spam')  # mensagem
