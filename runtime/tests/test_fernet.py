import unittest
from cryptography.fernet import Fernet


class FernetTest(unittest.TestCase):

    def test_create_key(self):
        fernet_key = Fernet.generate_key()
        print("fernet_key=> ", fernet_key)


if __name__ == '__main__':
    unittest.main()
