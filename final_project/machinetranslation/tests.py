# Import Libraries
import unittest
from translator import englishToFrench, frenchToEnglish

class testEnglishToFrench(unittest.TestCase):
    # Test englishToFrench function
    def test_englishToFrench(self):
        # Below are all the tests
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Bonjour'), 'Hello')
        self.assertEqual(englishToFrench(None), '')


class testFrenchtoEnglish(unittest.TestCase):
    # Test englishToFrench function
    def test_frenchtoEnglish(self):
        # Below are all the tests
        self.assertEqual(frenchToEnglish(None), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Hello'), 'Bonjour')

if __name__ == "__main__":
    unittest.main()