"""_summary_

Returns:
    _type_: _description_
"""

import  sys
from	_collections_abc import Iterable

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function. """

    if not isinstance(iterable, Iterable):
        print("Error: Wrong argumnets")
        sys.exit()

    try:
        function_to_apply(iter(iterable))
    except:
        print("Error: Iterable cannot be used by the function ")

    _it = iter(iterable)
    value = next(_it)
    for i in _it:
        value = function_to_apply(value, i)
    return value
