from .base_error import BaseUserException


class DBError(BaseUserException):
    msg = "Не удалось создать соединение"


class CreateUserError(BaseUserException):
    msg = "Не  удалось создать пользователя"


class ChangeUserDataError(BaseUserException):
    msg = "Не удалось изменить данные пользователя"
