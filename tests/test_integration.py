import unittest

import requests


class TestIntegration(unittest.TestCase):
    def test_index(self):
        response = requests.request(
            "GET",
            "http://0.0.0.0/",
        )
        self.assertEqual(response.status_code, 200)

        response = requests.request(
            "POST",
            "http://0.0.0.0/",
        )
        self.assertEqual(response.status_code, 200)




if __name__ == "__main__":
    unittest.main()
