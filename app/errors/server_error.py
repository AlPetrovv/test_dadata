from .base_error import BaseUserException


class PlacesError(BaseUserException):
    msg = "Не удалось получить данные о месте"


class GeolocateError(BaseUserException):
    msg = "Не удалось получить геолокацию места"


class DataError(BaseUserException):
    msg = "Токен не действителен "
