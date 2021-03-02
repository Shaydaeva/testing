import requests

"""
Входные данные:
VK_USER_ID - id пользователя (для проверки короткого имени использовать 'screen_name': '')
VK_TOKEN - специальный ключ доступа для идентификации в API
API_VERSION - используемая версия API
"""

VK_USER_ID_ACTIVE = 3028414
VK_USER_ID_NOT_ACTIVE = 60404741
VK_TOKEN = ''
API_VERSION = 5.101


def test_is_active():
    """
     Проверка существования пользователя VK через API.
    """
    response = requests.get("https://api.vk.com/method/users.get", params={'access_token': VK_TOKEN,
                                                                           'user_id': VK_USER_ID_ACTIVE,
                                                                           'v': API_VERSION})
    data = response.json()['response'][0].get('deactivated')
    assert data is None
