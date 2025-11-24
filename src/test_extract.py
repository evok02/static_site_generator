from extract import extract_images, extract_links
import unittest

class TestExtract(unittest.TestCase):
    def test_eq(self):
        case1 = "Test ![image](https://imgur.com/comic_book) test test"
        case2 = "dota dota dota [image](https://imgur.com/comic_book) test"
        case3 = "()() !(image)(http://imgur) test test"
        self.assertEqual(extract_images(case1), [("![image]", "(https://imgur.com/comic_book)")])
        self.assertEqual(extract_links(case2), [("[image]", "(https://imgur.com/comic_book)")])
        self.assertEqual(extract_images(case3), [])
        self.assertEqual(extract_links(case3), [])


