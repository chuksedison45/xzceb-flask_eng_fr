import unittest

from translator import *

class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french("Hello"), 'Bonjour')
        self.assertEqual(english_to_french('girl'), 'Fille')
        self.assertEqual(english_to_french('Boy'), 'Garçon')


class TestFrechToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english('Garçon'), 'Boy')
        self.assertEqual(french_to_english('Fille'), 'Daughter')

if __name__ == '__main__':
    unittest.main()


