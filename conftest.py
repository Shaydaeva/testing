import pytest


@pytest.fixture()
def ness_data():
    with open("auth_vk.ini", 'r') as file:
        access_token = file.readline()
    data = {'access_token': access_token,
            'VK_USER_ID': 3028414,
            'API_VERSION': 5.28,
            'url_api': "https://api.vk.com/method/"}
    return data


"""
"https://api.vk.com/method/users.get"

"""
