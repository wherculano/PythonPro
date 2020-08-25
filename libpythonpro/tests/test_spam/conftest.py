import pytest
from PythonPro.libpythonpro.spam.db import Conexao
# todas as fixtures criadas neste arquivo (que por padrão deve se chamar ConfTest)
# estarão disponíveis para todos os módulos do mesmo pacote (neste caso o pacote test_spam).


#  Fixtures para Setup do BD
@pytest.fixture(scope='session')
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
