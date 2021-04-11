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