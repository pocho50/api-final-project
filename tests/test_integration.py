import unittest

import requests


class TestIntegration(unittest.TestCase):
    #def test_index(self):
    #    response = requests.request("GET", "http://0.0.0.0/",)
    #    self.assertEqual(response.status_code, 200)

    #    response = requests.request("POST", "http://0.0.0.0/",)
    #    self.assertEqual(response.status_code, 200)

    def test_predict(self):
        files = [
            ("file", ("e3e0aafc5c1dab9f7743e63dcf4c8a83.mp4", open("tests/e3e0aafc5c1dab9f7743e63dcf4c8a83.mp4", "rb"), "video/mp4"))
        ]
        headers = {}
        payload = {}
        response = requests.request(
            "POST",
            "http://0.0.0.0/predict",
            headers=headers,
            data=payload,
            files=files,
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)
        self.assertEqual(data["scenes"]['0']["scale"], "LS")
        self.assertEqual(data['scenes']['0']["movement"], 'Motion')


if __name__ == "__main__":
    unittest.main()

