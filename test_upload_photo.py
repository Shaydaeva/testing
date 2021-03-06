import requests

"""
Тестирование загрузки фотографии в VK через API.
Входные данные:
VK_USER_ID - id пользователя
access_token - специальный ключ доступа для идентификации в API
API_VERSION - используемая версия API
"""


def test_create_new_album(ness_data):
    """
    Функция для проверки работоспособности создания альбома, загрузки фотографии и проверки
    её наличия в альбоме
    """
    # Проверка создания нового альбома
    response = requests.get(ness_data['url_api'] + "photos.createAlbum",
                            params={'access_token': ness_data['access_token'],
                                    'v': ness_data['API_VERSION'],
                                    'title': 'test2'})
    new_album = response.json()
    assert new_album.get('response') is not None

    new_album_id = new_album['response']['id']

    # Список фотографий в новом альбоме
    # Фотографий в альбоме еще нет, ожидаю 0
    response = requests.get(ness_data['url_api'] + "photos.get",
                            params={'access_token': ness_data['access_token'],
                                    'owner_id': ness_data['VK_USER_ID'],
                                    'v': ness_data['API_VERSION'],
                                    'album_id': new_album_id
                                    })
    count_photo = response.json()
    assert count_photo.get('response') is not None

    count_photo_before = count_photo['response']['count']

    # Получение адреса сервера для загрузки фото
    response = requests.get(ness_data['url_api'] + "photos.getUploadServer",
                            params={'access_token': ness_data['access_token'],
                                    'v': ness_data['API_VERSION'],
                                    'album_id': new_album_id
                                    })
    upload_url_data = response.json()
    assert upload_url_data.get('response') is not None

    upload_url = upload_url_data['response']['upload_url']

    # Загрузка фото на сервер
    response = requests.post(upload_url,
                             files={'file1': open('Koala.jpg', 'rb')},
                             params={'access_token': ness_data['access_token'],
                                     'v': ness_data['API_VERSION']})
    upload_photo = response.json()
    assert (upload_photo.get('server') is not None and
            upload_photo['photos_list'] is not None and
            upload_photo['hash'] is not None and
            upload_photo['aid'] is not None)

    # Сохранение фото в альбоме
    save_photo = requests.get(ness_data['url_api'] + "photos.save",
                              params={'access_token': ness_data['access_token'],
                                      'v': ness_data['API_VERSION'],
                                      'album_id': new_album_id,
                                      'server': upload_photo['server'],
                                      'photos_list': upload_photo['photos_list'],
                                      'hash': upload_photo['hash'],
                                      'aid': upload_photo['aid']
                                      })

    # Проверка нового списка фотографий
    # Загрузили 1 фото, ожидаю 1
    response = requests.get(ness_data['url_api'] + "photos.get",
                            params={'access_token': ness_data['access_token'],
                                    'owner_id': ness_data['VK_USER_ID'],
                                    'v': ness_data['API_VERSION'],
                                    'album_id': new_album_id
                                    })
    count_photo = response.json()
    assert count_photo.get('response') is not None
    count_photo_after = count_photo['response']['count']

    assert count_photo_before + 1 == count_photo_after
