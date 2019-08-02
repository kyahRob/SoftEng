import unittest
import main
import img2txt
import Sign

class Test(unittest.TestCase):
    def Login_Test(self):
        self.assertTrue(main.login_Test("Jerome"))
        self.assertFalse(main.CheckPass_Test(""))
        self.assertTrue(main.login_Test("Kate"))
        self.asserTrue(main.CheckPass_Test("123"))
        self.assertFalse(login_Test("Rico"))
                         
    def Signup_Test(self):
        self.assertTrue(Sign.Reg_Test("Gwen C", "gwc", "123", "123"))
        self.assertFalse(Sign.Reg_Test("Gwen C", "gwc", "123", "12345"))
        self.assertFalse(Sign.Reg_Test("", "Jerome", "123", "123"))
                         
    def ImageRecog(self):
        self.assertTrue(img2txt.recognimage_Test("/lanztest.png"))
                        
if __name__ == "__main__":
    unittest.main()
                     
