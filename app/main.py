import unittest
from main import get_external_ip

class TestMain(unittest.TestCase):
    def test_get_external_ip(self):
        ip = get_external_ip()
        self.assertIsNotNone(ip)

if __name__ == '__main__':
    unittest.main()

