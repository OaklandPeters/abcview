import abc
import types

#    Essentially a TypeRestriction(), 'type promotion' in C-terms
def ABCView(vog):
    """Create class which is the intersection of 'obj', with
    the abstract methods and properties of 'vog'; then inherits
    from 'vog' -- receiving its Mixin methods.    
    
    
    >>> obj = [0,1,2]
    >>> SeqView = ABCView(Sequence)
    >>> seq     = SeqView(obj)
      
    #Confirm that it DOES NOT have non-Sequence methods from list
    #    Such as .append (which list has, but Sequence does not)
    >>> seq.append(3)
    Traceback (most recent call last):
    AttributeError: 'SequencePromotion' object has no attribute 'append'
    
    #Observe: Changes to mutable view change the original object
    >>> MSeqView = ABCView(MutableSequence)
    >>> mseq     = MSeqView(obj)
    >>> mseq.append(3)
    >>> mseq
    [0, 1, 2, 3]
    >>> obj
    [0, 1, 2, 3]
    """
    assert(isinstance(vog,abc.ABCMeta)), "vog must be an abstract class."
    def init(self,obj):
        #@todo: self.__obj = weakref.weakref(obj)
        vog = self.__vog
        assert(isinstance(obj,vog)), str.format(
            "'obj' does not meet {0}.",vog.__name__)
        assert(not isinstance(obj,type)), str.format(
             "'obj' is not an instance.")
        self.__obj = obj
    redirector = lambda self: self.__obj
    
    
    
    new_attrs = {
        '__vog':vog,
        '__init__':init,
        #'__init__':lambda self,obj: setattr(self,'__obj',obj)
    }
    
    for name in get_abstracts(vog):
        vog_attr = getattr(vog,name)
        if isinstance(vog_attr,types.MethodType):
            new_attrs[name] = binding_wrapper(name,redirector)
        #abstractproperty ...
        else:   
            new_attrs[name] = property(lambda self: getattr(self.__obj,name))
    
    #Tentative: Add repr
    if hasattr(vog,'__repr__'):
        new_attrs['__repr__'] = binding_wrapper('__repr__',redirector)
    
            
    new_name = vog.__name__+'Promotion'
    #new_bases: will ensure that the new object inherits mixin methods from VOG
    new_bases = (vog,)
    new_cls = type(new_name,new_bases,new_attrs)
    return new_cls


#==============================================================================
#    Local Utility Functions
#==============================================================================
def binding_wrapper(name, redirector=None):
    """
    @binding_wrapper()
    """
    if redirector == None:
        redirector = lambda self: self
    assert(callable(redirector)), "Redirector not Callable."
        
    def wrapped(self,*args,**kwargs):
        #obj = self.__obj
        obj = redirector(self)
        attr = getattr(obj,name)
        return attr(*args,**kwargs)
    return wrapped
#    if wraps == None:
#        return wrapped
#    elif isinstance(wraps,Callable):
#        return functools.wraps(wraps)(wrapped)
#    else:
#        raise TypeError("Invalid 'wraps' of type: "+type(wraps).__name__)


def is_abstract(func):
    try:
        return func.__isabstractmethod__
    except AttributeError:
        return False
    
def get_abstracts(vog):
    """Where 'vog' is an abstract base class
    >>> 
    >>> get_abstracts(Sequence)
    ['__getitem__', '__len__']
    """
    return [
        name
        for name in dir(vog)
        if is_abstract(getattr(vog,name))
    ]




