# Общее описание #

В файлах test_user_is_active.py и test_upload_photo.py содержатся функции для проверки учетной записи пользователя и возможности создания альбома и загрузки фото.  
Библиотеки, необходимые для работы, в файле requirments.txt  
.gitignore упразднён в рамках данного проекта
***
### Константы
VK_USER_ID - id пользователя  
VK_TOKEN - специальный ключ доступа для идентификации в API  
API_VERSION - используемая версия API  
/* Для test_upload_photo.py необходимо изображение (для примера Koala.jpg)
***
### Запуск и описание тестов
Тесты запускать через коммандную строку с помощью pytest <file_name>
***
###### test_user_is_active.py
Тест проверяет существование пользователя в социальной сети при помощи id или короткого имени  
Тест пройден, если пользователь существует  
Тест провален, еси пользователь удален или не создан

###### test_upload_photo.py
Сценарий проверки возможности создания нового альбома, загрузки фотографии в этот альбом и проверки её загрузки  
Тест пройден, если создался альбом и фото успешно загрузилось  
Тест провален в случае, если не создался альбом или фото не удалось загрузить
***
### Возможные доработки
+ Возможность проверки пользователей списком в test_user_is_active.py
+ Декомпозиция функции в test_upload_photo.py для разбиения проверок, добавление удаления после теста
+ Расширение зоны покрытия, например, подобная проверка функциональности стены, видео, групп
+ Удаление неактивных пользователей из списка друзей
***
