import vk
import getpass


APP_ID = 7777325


def get_login_pass():
    login = input("user_login: ")
    password = getpass.getpass(prompt="user_password: ")
    return login, password


def auth_vk_password():
    login, password = get_login_pass()
    try:
        session = vk.AuthSession(app_id=APP_ID,
                                 user_login=login,
                                 user_password=password,
                                 scope=4
                                 )
    except vk.exceptions.VkAuthError:
        print('Incorrect login/password')
    else:
        with open("auth_vk.ini", 'w') as file:
            file.writelines(session.access_token)
        return session


def auth_vk_token():
    try:
        file = open("auth_vk.ini", 'r')
    except IOError as e:
        access_token = auth_vk_password().access_token
    else:
        with file:
            access_token = file.readline()

    session = vk.Session(access_token=access_token)

    return session


auth_vk_token()
