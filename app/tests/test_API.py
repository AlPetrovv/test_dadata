import os
import unittest
from utils.user_fetch import UserDadata


class Test(unittest.TestCase):
    test_token: str = os.environ.get("TOKEN")

    def test_request(self) -> None:
        """
        checking state of API
        """
        u = UserDadata(self.test_token)
        res = u.send_check_request()
        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main()
