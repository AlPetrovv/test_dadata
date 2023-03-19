class BaseUserException(Exception):
    """
    Base class for errors
    """

    msg: str = None

    def __init__(self, obj, message: str = ""):
        self.message = self.msg or message
        super().__init__(obj)

    def __str__(self):
        return f"{self.message}. \nОписание ошибки: {self.args} "
