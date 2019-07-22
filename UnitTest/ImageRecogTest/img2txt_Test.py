import unittest
import img2txt

class TestLogin(unittest.TestCase):

    def testBrowseimage(self):
        self.assertEqual(browseimage("/robtest.png"), "robtest")

    def testRecognimage(self):
        self.assertEqual(recognimage("/robtest.png"), "ROB8")

if __name__ == '__main__':
    unittest.main()
                        
    
