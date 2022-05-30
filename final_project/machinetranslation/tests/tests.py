# Import Libraries
import unittest
from translator import englishToFrench, frenchToEnglish

class testEnglishToFrench(unittest.TestCase):
    # Test englishToFrench function
    def test_englishToFrench(self):
        # Below are all the tests
        self.assertEqual(englishToFrench(None), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class testFrenchtoEnglish(unittest.TestCase):
    # Test englishToFrench function
    def test_frenchtoEnglish(self):
        # Below are all the tests
        self.assertEqual(frenchToEnglish(None), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')