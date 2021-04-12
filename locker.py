import string
from random import choice


class User:
    """
    create User class that generates new instances of a user.
    """
    user_list = []

    def __init__(self, username, password):
        """
        method defining the user properties
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        A method that saves a new user instance into the user list
        """
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        """
        delete_account method deletes a  saved account from the list
        """
        User.user_list.remove(self)

    def get_user(self):
        for user in User.user_list:
            if user.username == self.username and user.password == self.password:
                return True
        return False

    def find_credentials(self):
        credentials = [credential for credential in Credentials.credentials_list if
                       credential.username == self.username and credential.password == self.password]
        return credentials

    def login(self):
        for user in self.user_list:
            if user.username == self.username and user.password == self.password:
                return Credentials.credentials_list

        return False


class Credentials:
    credentials_list = []

    def __init__(self, credential, username, password=None):
        self.username = username
        self.password = password
        self.credential = credential

    def save_credential(self):
        """
        Method that saves a user's credentials to a credential's list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.
        """
        for credential in cls.credentials_list:
            if credential.credential == account:
                return credential

    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.credential == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list
        """
        return cls.credentials_list

    @staticmethod
    def generate_random_password(length=None):
        """
        Method that generates a random alphanumeric password
        """
        if length is None:
            length = 10

        my_str = string.ascii_uppercase + string.digits + string.ascii_lowercase
        return ''.join(choice(my_str) for _ in range(length))
