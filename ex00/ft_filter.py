"""_summary_

Yields:
    _type_: _description_
"""

import  sys
from	_collections_abc import Iterable

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function. """

    if not isinstance(iterable, Iterable):
        print("Error: Wrong argumnets")
        sys.exit()

    try:
        function_to_apply(iter(iterable))
    except:
        print("Error: Iterable cannot be used by the function ")

    for i in iterable:
        if function_to_apply(i) is True:
            yield i
