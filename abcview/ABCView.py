

class ABCView(object):
    """
    Should be usable as a context-manager:
    with ABCView(myvar, MutableSequence) as value:
        value.append(...)
    """