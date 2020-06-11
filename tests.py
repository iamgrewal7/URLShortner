import unittest
from lib import UrlShortner
from random import randint

class TestUrlShortner(unittest.TestCase):
    def test_conversion(self):
        for _ in range(10**6):
            _id = randint(1, 999999)
            short_url = UrlShortner.id_to_url(_id)
            self.assertEqual(UrlShortner.url_to_id(short_url), _id)

if __name__ == '__main__':
    unittest.main()
