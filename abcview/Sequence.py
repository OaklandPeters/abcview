import collections

class SequenceView(collections.Sequence):
    def __init__(self, wrapped):
        if not isinstance(wrapped, collections.Sequence):
            raise TypeError("'wrapped' must be a 'Sequence'.")
        if hasattr(wrapped, '_wrapped'):
            raise AttributeError("'wrapped' must not have a '_wrapped' method.")
        self._wrapped = wrapped
    
    # Re-implement abstract methods - referencing self._wrapped
    def __getitem__(self, key):
        return self._wrapped.__getitem__(key)
    def __len__(self):
        return self._wrapped.__len__()
    def __contains__(self, element):
        return self._wrapped.__contains__(element)
