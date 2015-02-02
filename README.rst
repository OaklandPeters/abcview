package-tempalte
===================

Overview
----------
The concept of an ABCView is this::

    You can take an instance object, which meets some abstract interface,
    and "wrap" that instance with the interface, to get an object which:

    (1) For abstract methods, uses the implementation of the original object
    (2) For mixin-methods (ie methods on the interface which are 'derived'
        from the abstract methods), uses the implementation on the interface,
    (3) For instance-methods on the original object, those methods are not
        accessible from the wrapped-object
    (4) Changes/mutations of the wrapped-object effect the underlying object.


Example
---------
::
    from collections import Sequence
    my_sequence = ['a', 'b', 'c']
    sequence_view = ABCView(myseq, Sequence)

    sequence_view.index('a')  # 0

    # valid on lists, but invalid on sequences
    # hence, this raises an exception here
    sequence_view.insert(3, 'd')  


Extended Example
------------------
ABCView can also be used to provide more uniform and predictable behavior on custom objects.
For example, consider an object that meets the abstract methods of a MutableMapping, but
for which you want to use the mixins from MutableMapping (popitem, update, setdefault)::

    from collections import MutableMapping

    class MyMapping(object):
        """Implements abstract methods from MutableMapping."""
        def __init__(self, data):
            self.data = data
        def __getitem__(self, key):
            return self.data[key]
        def __setitem__(self, key, value):
            self.data[key] = value
        def __delitem__(self, key):
            del self.data[key]
        def __iter__(self):
            return iter(self.data)
        def __len__(self):
            return len(self.data)
        def __contains__(self, other):
            return other in self.data

    mine = MyMapping({'a':1, 'b':2})
    mm_view = ABCView(mine, MutableMapping)

    # Abstract methods same in both cases
    assert mine['a'] == mm_view['a']
    # The wrapped view has access to MutableMapping mixins, like .get
    try:
        mine.get('b')
    except AttributeError:
        pass  # Fails
    assert mm_view.get('b') == 2



Contributors
-------------
Oakland John Peters <oakland.peters@gmail.com>


License
---------
Available under the ``MIT license <http://opensource.org/licenses/MIT/>``_.

Copyright (c) 2014, Oakland John Peters.

