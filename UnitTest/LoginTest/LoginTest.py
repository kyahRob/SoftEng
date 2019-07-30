import unittest
import LogIn
import signup
class TestLogin(unittest.TestCase):

    def testLog_Test(self):
        self.assertTrue(Log_Test("Jerome", "123"))
        self.assertFalse(Log_Test("Jacob", "456"))
        self.assertTrue(Log_Test("Kate", "123"))

    def testRehistro_Test(self):
        self.assertTrue(Rehistro_Test("Rey", "rey4@yahoo.com", "123"))
        self.assertFalse(Rehistro_Test("", "", ""))

if __name__ == '__main__':
    unittest.main()
                        
    
