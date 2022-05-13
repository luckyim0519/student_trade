"""
File made by Lucky and Justin(Taehee) Cha

All copyrighted materials are owned by Lucky and Justin. 
2022, May, 11th
"""
from Store_item import Store_item
from typing import List



class User():
    """
    A user class.
    
    === Private Attributes ===
    _name: the name of this User
    _username: the username of this User
    _email: the Email of this User
    _posted_store_items: a list of items posted by this User

    === Representation Invariants ===
    _posted_store_items: this list does not contain any duplicate items of any sort.
    """
    _name: str
    _username: str
    _email: str
    _posted_store_items: List[Store_item]
    def __init__(self, n: str, un: str, e: str) -> None:
        """
        initialize an User object
        """
        self._name = n
        self._username = un
        self._email = e
        self._posted_store_items = []

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

    def buy_item(self, item: Store_item) -> bool:
        """
        Return True iff Store_item in item has been bought successfully by this User
        """
        #TODO

    def delete_item(self, item: Store_item) -> bool:
        """
        Remove this item from _posted_store_items list and from the database

        return True iff Store_item in item has been deleted successfully

        Precondition: Store_item in item exists in _posted_store_items of this User
        """
        self._posted_store_items.remove[item]
        #TODO