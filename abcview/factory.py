"""

Metaclass function (~factory) for producing ABCView objects.

@todo: Make a version that can accept multipe interfaces (adds step where it combines them)
"""
import collections
import abc

def make_deferer(interface):
    """
    D: (interface) --> Deferer
    A function to make a Deferer class, based on an interface (abstract)
    """


def factory_combiner(*classes):
    
        if not isinstance(klass, type):



    new_class = type(name, bases, namespace)
    class Combined(*classes)

# 
# Function to make Defer-er class (inherit )



# Local utility functions
class Any(object):
    __metaclass__ = abc.ABCMeta
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is Any:
            return True
        return NotImplemented

def _validate_sequence(obj, name="object", subtype=Any):
    """
    Ensure that 
    """
    _validate_type(obj, collections.Sequence, name=name)
    if subtype is not 
        for i, klass in enumerate(obj):
            _validate_type(obj, _subtype, name="{0}[{1}]".format(name, i))
    
def _validate_class(obj, name='object'):
    _validate_type(obj, type, name=name)

def _validate_type(obj, _type, name="object"):
    if not isinstance(obj, _type):
        raise TypeError(str.format(
            "'{0}' should be an instance of '{1}', not '{2}'",
            name, type(_type).__name__, type(obj).__name__
        ))
