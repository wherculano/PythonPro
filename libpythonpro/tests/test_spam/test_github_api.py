from unittest.mock import Mock
from PythonPro.libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {'login': 'wherculano', 'id': 26460999,
                                   'avatar_url': 'https://avatars2.githubusercontent.com/u/26460999?v=4'
                                   }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('wherculano')
    assert 'https://avatars2.githubusercontent.com/u/26460999?v=4' == url
