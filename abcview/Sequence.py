"""
This is an example of what ABCViews of an abstract class would look like.

Necessary parts:
(1) Inherit from the abstract class (interface)
(2) Override __init__ to accept an instance object (wrapped), which meets the interface
(3) Override the abstract methods, with functions that defer to the method of the same name, defined on the wrapped object (IE self.__len__() --> self._wrapped.__len__()).
(4) Mixin methods are left unchanged (since they refer only to abstract methods or other mixin methods).
"""
import collections

# (1) Inherit from the interface
class SequenceView(collections.Sequence):
    # (2) Override the constructor
    def __init__(self, wrapped):
        if not isinstance(wrapped, collections.Sequence):
            raise TypeError("'wrapped' must be a 'Sequence'.")
        if hasattr(wrapped, '_wrapped'):
            raise AttributeError("'wrapped' object must not have a '_wrapped' method.")
        self._wrapped = wrapped
    
    # (3) Override abstract methods
    def __getitem__(self, key):
        return self._wrapped.__getitem__(key)
    def __len__(self):
        return self._wrapped.__len__()
    def __contains__(self, element):
        return self._wrapped.__contains__(element)

    # (4) Mixin methods unchanged
