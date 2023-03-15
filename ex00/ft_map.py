"""_summary_

Yields:
    _type_: _description_
"""

import  sys
from	_collections_abc import Iterable

def ft_map(function, iterable: Iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function. """

    if not isinstance(iterable, Iterable):
        print("Error: Wrong arguments passed.")
        sys.exit()

    try:
        function(iter(iterable))
    except:
        print("Error: Iterable cannot be used by the function ")

    for i in iterable:
        yield function(i)
