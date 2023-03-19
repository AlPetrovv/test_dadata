class UserValidator:  # can do it as function
    """
    class which checks token
    """
    EXIT_COMMAND: list = ["exit", "выход", "'выход'", "'exit'"]

    def __init__(self, s: str):
        self.s = s

    def check_data(self) -> dict | None:
        res: dict = {}
        string: str = input(f"{self.s}: ")
        if string in self.EXIT_COMMAND:
            return None
        if not string.isascii():
            res['error'] = f"{self.s} должен состоять из английских символов и букв"
            return res
        res["access"] = string
        return res
