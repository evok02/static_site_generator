from main import extract_title
import unittest




class TestExtractTitle(unittest.TestCase):
    markdown = """
    some text 

    some text 

    ## Title

    # Title

    some text

    some text

    some text

    """



    def test_extract_eq(self):
        self.assertEqual(extract_title(self.markdown), "Title")
        self.assertNotEqual(extract_title(self.markdown), "#Title")
        self.assertNotEqual(extract_title(self.markdown), "##Title")




