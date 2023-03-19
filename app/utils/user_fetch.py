from dadata import Dadata
from httpx import HTTPStatusError, LocalProtocolError
from errors.server_error import DataError, GeolocateError, PlacesError
from utils.validators import UserValidator


class UserDadata:
    """
    class descriptions user and to do actions
    """
    dadata: Dadata
    BASE_URL = ""

    def __init__(self, token: str, lang: str = 'ru'):
        self.lang = lang
        self.__token = token

    def get_user_data(self) -> tuple:
        return self.token, self.lang

    def send_check_request(self) -> bool:
        """
        sending a test request to dadata
        """
        self.dadata: Dadata = Dadata(self.token)
        try:
            res: list = self.dadata.suggest(name="address", query="москва", language=self.lang, count=1)
            if not res:
                return False
            return True
        except (HTTPStatusError, LocalProtocolError) as e:
            print(DataError(e))

    def change_data(self) -> bool:
        """
        The function changes data and checks it
        """
        print("Действия: \n"
              "t - изменить token \n"
              "l - изменить язык\n"
              "exit или выход - выход из действия")
        user_data = self.get_user_data()  # imitation rollback
        while True:
            answer = input("Действие: ").strip()
            match answer:

                case "l":
                    _lang = input("Язык (ru/en): ").lower().strip()
                    if _lang in ["exit", 'выход']:
                        return False
                    self.lang = _lang if _lang == "en" else "ru"

                case "t":
                    if _token := UserValidator("token").check_data():
                        if error := _token.get("error"):
                            print(error)
                            continue
                        elif token := _token.get("access"):
                            self.token = token
                    else:
                        return False

                case "exit" | "выход":
                    return False
                case _:
                    print("Неправильный ввод действия")
                    continue
            if self.send_check_request():
                break
            self.token, self.lang = user_data
        return True

    def execute_places(self, query: str) -> list | None:
        """
        Receiving list of  places(addresses)
        """
        try:
            res = self.dadata.suggest(name='address', query=query, language=self.lang)
            if res:
                return res
            return None
        except Exception as e:
            print(PlacesError(e))

    def get_geolocate(self, query: str) -> dict | None:
        """
        Receiving specific place(address)
        """
        try:
            res: list = self.dadata.suggest(name="address", query=query, language=self.lang, count=1)
            return res[0] if res else None
        except Exception as e:
            print(GeolocateError(e))

    @property
    def token(self):
        return f"{self.__token}"

    @token.setter
    def token(self, new_token):
        self.__token = new_token
