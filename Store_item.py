"""
File made by Lucky and Justin(Taehee) Cha

All copyrighted materials are owned by Lucky and Justin. 
2022, May, 11th
"""

from Users import User


class Store_item():
    """
    A class for items on the website

    === Private Attributes ===
    _name: name of the item
    _id: id of the item
    _og_user: the user that posted this Store_item
    """
    _name: str
    _id: int
    _og_user: User

    def __init__(self, n: str, i: int, u: User) -> None:
        self._name = n
        self._id = i
        self._og_user = u
