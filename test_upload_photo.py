import requests

"""
Тестирование загрузки фотографии в VK через API.
Входные данные:
VK_USER_ID - id пользователя
VK_TOKEN - специальный ключ доступа для идентификации в API
API_VERSION - используемая версия API
"""

VK_USER_ID = 3028414
VK_TOKEN = ''
API_VERSION = 5.101


def test_create_new_album():
    """
    Функция для проверки работоспособности создания альбома, загрузки фотографии и проверки
    её наличия в альбоме
    """
    # Проверка создания нового альбома
    new_album = requests.get("https://api.vk.com/method/photos.createAlbum",
                             params={'access_token': VK_TOKEN,
                                     'v': API_VERSION,
                                     'title': 'test2'}).json()
    assert new_album.get('response') is not None

    new_album_id = new_album['response']['id']

    # Список фотографий в новом альбоме
    # Фотографий в альбоме еще нет, ожидаю 0
    count_photo_before = requests.get("https://api.vk.com/method/photos.get",
                                      params={'access_token': VK_TOKEN,
                                              'owner_id': VK_USER_ID,
                                              'v': API_VERSION,
                                              'album_id': new_album_id
                                              }).json()['response']['count']

    # Получение адреса сервера для загрузки фото
    upload_url = requests.get("https://api.vk.com/method/photos.getUploadServer",
                              params={'access_token': VK_TOKEN,
                                      'v': API_VERSION,
                                      'album_id': new_album_id
                                      }).json()['response']['upload_url']

    # Загрузка фото на сервер
    upload_photo = requests.post(upload_url,
                                 files={'file1': open('Koala.jpg', 'rb')},
                                 params={'access_token': VK_TOKEN, 'v': API_VERSION}).json()

    # Сохранение фото в альбоме
    save_photo = requests.post("https://api.vk.com/method/photos.save",
                               params={'access_token': VK_TOKEN,
                                       'v': API_VERSION,
                                       'album_id': new_album_id,
                                       'server': upload_photo['server'],
                                       'photos_list': upload_photo['photos_list'],
                                       'hash': upload_photo['hash'],
                                       'aid': upload_photo['aid']
                                       })

    # Проверка нового списка фотографий
    # Загрузили 1 фото, ожидаю 1
    count_photo_after = requests.get("https://api.vk.com/method/photos.get",
                                     params={'access_token': VK_TOKEN,
                                             'owner_id': VK_USER_ID,
                                             'v': API_VERSION,
                                             'album_id': new_album_id
                                             }).json()['response']['count']

    assert count_photo_before + 1 == count_photo_after
