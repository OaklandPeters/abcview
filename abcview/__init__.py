"""

The concept of an ABCView is this:
you can take an instance object, which meets some abstract interface,
and "wrap" that instance with the interface, to get an object which:
(1) For abstract methods, uses the implementation of the original object
(2) For mixin-methods (ie methods on the interface which are 'derived'
    from the abstract methods), uses the implementation on the interface,
(3) For instance-methods on the original object, those methods are not
    accessible from the wrapped-object
"""
