"""_summary_

Yields:
    _type_: _description_
"""

import  time

start = time.time()

N = 3333

def ft_progress( lst ):
    """_summary_

    Args:
        lst (_type_): _description_

    Yields:
        _type_: _description_
    """
    prev = time.time()
    new = prev
    for i in lst:
        if i == 1:
            new = time.time() - prev
        yield i
        print("ETA: {:.2f}s [{:>3}%][{:<11}] {:>3}/{} | elapsed time {:>3.2f}s".format( \
                (new) * (len(lst)), \
                int((i/len(lst))*100), \
                "="*int(((i+1)/len(lst))*10)+">", \
                i, \
                len(lst) - 1, \
                time.time() - start), \
            end="\r")
