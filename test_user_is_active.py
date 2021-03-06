import requests

"""
Входные данные:
VK_USER_ID - id пользователя (для проверки короткого имени использовать 'screen_name': '')
VK_USER_ID_NOT_ACTIVE - пример неактивного id пользователя, при котором тест провалится
access_token - специальный ключ доступа для идентификации в API
API_VERSION - используемая версия API
"""


VK_USER_ID_NOT_ACTIVE = 60404741


def test_is_active(ness_data):
    """
     Проверка существования пользователя VK через API.
    """
    response = requests.get(ness_data['url_api'] + "users.get", params={'access_token': ness_data['access_token'],
                                                                           'user_id': ness_data['VK_USER_ID'],
                                                                           'v': ness_data['API_VERSION']})
    data = response.json()
    assert data['response'][0].get('deactivated') is None
