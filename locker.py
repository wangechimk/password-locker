import string
from random import choice


class User :
    """
    create User class that generates new instances of a user.

    """
    user_list = []

    def __init__(self,username,password):
        """
        method defining the user properties
        """

        self.username = username
        self.password =password

    def save_user(self):
            """
            A method that saves a new user instance into the user list
            """

            User.user_list.append(self)

            def get_user(self):
        for user in User.user_list:
            
            if user.username == self.username and user.password == self.password:
                return True
        return False

    def find_credentials(self):
        credentials = [credential for credential in Credentials.credentials_list if credential.username == self.username and credential.password == self.password]
        return credentials



class Credentials:
    Credentials_list =[]       

    def __init__(self, credential, username, password=None):
        self.username = username
        self.password = password
        self.credential = credential

        def save_credential(self):
        """
        Method that saves a user's credentials to a credential's list
        """

       Credentials.credentials_list.append(self)
