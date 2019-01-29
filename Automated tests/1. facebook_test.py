import unittest

from facebook import Facebook

class FacebookTest(unittest.TestCase):
    # Is there?
    def test_initialization(self):
        facebook = Facebook()
        self.assertTrue(facebook)

if __name__ == '__main__':
    unittest.main()