import unittest
from locker import User, Credentials


class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """

    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.user = User('WangechiKimani', '123Pass')
        self.credentials = Credentials('Twitter', 'WangechiKimani', '123Pass')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.user.username, 'WangechiKimani')
        self.assertEqual(self.user.password, '123Pass')

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list

        """
        self.user.save_user()
        self.assertGreater(len(User.user_list), 0)

    def test_get_user(self):
        self.user.save_user()

        self.assertIsNot(User.get_user(User('WangechiKimani', '123Pass')), False)

    def test_save_credentials(self):
        self.credentials.save_credential()
        self.assertGreater(len(Credentials.credentials_list), 0)

    def test_generate_random_password_with_predefined_length(self):
        credentials = Credentials('twitter', 'WangechiKimani')
        password = credentials.generate_random_password(2)
        self.assertEqual(len(password), 2)

    def test_generate_random_password_with_standard_length(self):
        credentials = Credentials('twitter', 'WangechiKimani')
        password = credentials.generate_random_password()
        self.assertEqual(len(password), 10)

    def test_find_credentials(self):
        self.credentials.save_credential()
        self.assertEqual(len(self.user.find_credentials()), 0)

    def tearDown(self):
        """      method that does clean up after each test case has run.
        """

        Credentials.credentials_list = []

    def test_save_many_accounts(self):
        """
        test to check if we can save multiple credentials objects to our credentials list
        """
        self.credentials.save_credential()
        test_credential = Credentials("Twitter", "WangechiKimani", "456Pass")
        test_credential.save_credential()
        self.assertGreater(len(Credentials.credentials_list), 1)

    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.credentials.save_credential()
        self.credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 0)

    def test_find_credential(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.credentials.save_credential()
        credential = self.credentials.find_credential("Twitter")
        self.assertEqual(self.credentials.credential, credential.credential)

    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.credentials.save_credential()
        the_credential = Credentials("Twitter", "WangechiKimani", "456Pass")
        the_credential.save_credential()
        credential_is_found = Credentials.if_credential_exist("Twitter")
        self.assertTrue(credential_is_found)

    def test_display_all_saved_credentials(self):
        """
        method that displays all the credentials that has been saved by the user
        """

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)


if __name__ == "__main__":
    unittest.main()
