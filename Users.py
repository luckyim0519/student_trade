"""
File made by Lucky and Justin(Taehee) Cha

All copyrighted materials are owned by Lucky and Justin. 
2022, May, 11th
"""

class User():
    """
    A user class.
    
    === Private Attributes ===
    _name: the name of this User
    _username: the username of this User
    _email: the Email of this User
    """
    _name: str
    _username: str
    _email: str
    def __init__(self, n: str, un: str, e: str) -> None:
        """
        initialize an User object
        """
        self._name = n
        self._username = un
        self._email = e

    def __str__(self) -> str:
        """
        to string method for User
        """
        return 'This is User ' + self._username + '. Real name is ' + self._name + '. Email is ' + self._email + '.'
    
    def get_username(self) -> str:
        """
        return the username of this User
        """
        return self._username
    
    def get_email(self) -> str:
        """
        return the email of this User
        """
        return self._email

    def get_name(self) -> str:
        """
        return the name of this User
        """
        return self._name