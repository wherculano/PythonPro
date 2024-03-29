from unittest.mock import Mock
import pytest
from PythonPro.libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars2.githubusercontent.com/u/26460999?v=4'
    resp_mock.json.return_value = {'login': 'wherculano', 'id': 26460999,
                                   'avatar_url': url
                                   }
    get_mock = mocker.patch('PythonPro.libpythonpro.github_api.requests.get')  # volta para a lib original apos o teste.
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('wherculano')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('wherculano')
    assert 'https://avatars.githubusercontent.com/u/26460999?v=4' == url
