import time
from .user_fetch import UserDadata
from .validators import UserValidator

USER_LANGUAGE = [
    "ru", "en"
]
print("Здравствуйте, для получения данных нужно получить несколько параметров: \n"
      "1. Токен (token) для сервиса dadata(если у вас его нет, то нужно зарегистрироваться на сайте \n"
      "https://dadata.ru/profile/#info и получить его в личном кабинете.\n"
      "2. Язык (language) для получения ответа русский(ru) или английский(en), по умолчанию ru\n"
      "Для выхода из системы введите 'exit' или 'выход'")

time.sleep(2)  # animation)


def set_user_language() -> str | None:
    lang: str = input("Язык ru или en, если хотите оставить русский, нажмите enter: ")
    if lang in USER_LANGUAGE:
        return lang
    return "ru"


def get_user_settings() -> UserDadata | None:
    """
    Function which getting data's user:
    1. since getting data's user
    2. checking them( test send to API and ascii checking )
    3. return class with user params
    """
    while True:
        _token: dict | None = UserValidator("token").check_data()  # get token and check it
        if not _token:
            return
        if error := _token.get("error"):
            print(error)
            continue
        token: str = _token.get("access")

        lang: str = set_user_language()
        u = UserDadata(token=token, lang=lang)
        if u.send_check_request():
            break

    return u
