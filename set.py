""" 
file: set.py
An abstraction for classes that implement set operations
author: vinay more
"""

from abc import abstractmethod, ABCMeta

class SetType( metaclass=ABCMeta ):
    """
    A collection of keys where no key may be in the set more than once.
    Note that this is a set, not a map, so there are only keys, not values.
    """

    __slots__ = 'size'

    def __init__( self ):
        """
        This abstract class just keeps the state information about the
        'size', or number of entries in the set.
        (So, all sets must manually maintain their number of entries.)
        """
        self.size = 0

    @abstractmethod
    def contains( self, obj ):
        """
        Is the given obj in the set?
        The answer is determined through use of the '==' operator,
        i.e., the __eq__ method.
        :return: True iff obj or its equivalent has been added to this set
                       and not removed
        """
        return False

    @abstractmethod
    def add( self, obj ):
        """
        Insert a new object into the set.
        Do not add if self.contains(obj).
        :param obj: the object to add
        :return: None
        :post: self.contains( obj )
        """

    @abstractmethod
    def remove( self, obj ):
        """
        Remove an object from the set.
        :param obj: the value to remove
        :return: None
        :post: not self.contains( obj )
        """
        pass

    @abstractmethod
    def __iter__( self ):
        """
        Build an iterator.
        :return: an iterator for the current elements in the set
        """
        return ()
