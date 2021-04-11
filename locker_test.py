import unittest
from locker import User

class UserTest(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('WangechiKimani','123Pass')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'WangechiKimani')
        self.assertEqual(self.new_user.password,'123Pass')

if __name__ == "__main__":
    unittest.main()
