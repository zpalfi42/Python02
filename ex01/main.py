"""_summary_
"""

class ObjectC(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def __init__(self):
        pass

def what_are_the_vars(*args, **kwargs):
    """_summary_

    Returns:
        _type_: _description_
    """
    obj = ObjectC()
    i = 0
    for attr in args:
        setattr(obj, "var_" + str(i), attr)
        i += 1
    for attr in kwargs:
        if attr in dir(obj):
            return None
        setattr(obj, attr, kwargs.get(attr))
    return obj

def doom_printer(obj):
    """_summary_

    Args:
        obj (_type_): _description_
    """
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")
 
if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
