import os
from unittest import TestCase
from unittest.mock import Mock
import settings

from werkzeug.datastructures import FileStorage

import utils


class TestUtils(TestCase):
    def test_allowed_file(self):
        self.assertFalse(utils.allowed_file("cat.JPG"))
        self.assertFalse(utils.allowed_file("cat.jpeg"))
        self.assertFalse(utils.allowed_file("cat.JPEG"))
        self.assertFalse(utils.allowed_file("../../car.PNG"))
        self.assertFalse(utils.allowed_file("/usr/var/src/car.gif"))

        self.assertTrue(utils.allowed_file("cat.mp4"))
        self.assertTrue(utils.allowed_file("cat.ogg"))
        self.assertTrue(utils.allowed_file("cat.webm"))


    def test_get_file_hash(self):
        filename = "tests/movie.mp4"
        md5_filename = "deab000c5012b3e9dafe8262046a556c.mp4"
        with open(filename, "rb") as fp:
            file = FileStorage(fp)

            # Check the new filename is correct
            _, new_filename = utils.directory_file_hash(file)
            self.assertEqual(md5_filename, new_filename, new_filename)

            # Check the file content is still readable!
            self.assertTrue(file.read() != b"")

    def test_valid_url_youtube(self):
        url = 'https://www.youtube.com/watch?v=qXYb8R3_B0k'

        self.assertTrue(utils.allowed_url(url))
        self.assertFalse(utils.allowed_url('blabla'))
        
