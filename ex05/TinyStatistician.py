"""_summary_
"""

import  numpy as np

class   TinyStatistician:
    """_summary_
    """

    def mean(self, _x):
        """_summary_

        Args:
            _x (_type_): _description_
        """

        _t = 0
        for _i in _x:
            if (isinstance(_i, list) or isinstance(_i, np.ndarray)):
                for _v in _i:
                    _t += _v
            else:
                _t += _i
        return _t / len(_x)

    def median(self, _x):
        """

        Args:
            _x (_type_): _description_
        """
        if (isinstance(_x[0], list) or (isinstance(_x[0], np.ndarray))):
            _l = []
            for _i in _x:
                if isinstance(_i, np.ndarray):
                    print(_i)
                    for _v in _i:
                        _l.append(_v)
                else:
                    _l += _i
        else:
            _l = _x
        _l.sort()
        if len(_l) % 2 == 0:
            _m = (_l[int(len(_l) / 2)] + _l[int((len(_l) / 2 ) - 1)]) / 2
        else:
            _m = _l[int(len(_l) / 2)]
        return _m

    def quartiles(self, _x):
        """_summary_

        Args:
            _x (_type_): _description_
        """
        if (isinstance(_x[0], list) or (isinstance(_x[0], np.ndarray))):
            _l = []
            for _i in _x:
                if isinstance(_i, np.ndarray):
                    for _v in _i:
                        _l.append(_v)
                else:
                    _l += _i
        else:
            _l = _x
        _l.sort()
        _q = []
        _s1 = (len(_l) + 1) / 4
        _s3 = 3 * _s1
        _d1 = _s1 - int(_s1)
        _d3 = _s3 - int(_s3)
        _q.append(_l[int(_s1) - 1] + _d1 * (_l[int(_s1)] - _l[int(_s1) - 1]))
        _q.append(_l[int(_s3) - 1] + _d3 * (_l[int(_s3)] - _l[int(_s3) - 1]))
        return _q

    def var(self, _x):
        """_summary_

        Args:
            _x (_type_): _description_
        """
        if (isinstance(_x[0], list) or (isinstance(_x[0], np.ndarray))):
            _l = []
            for _i in _x:
                if isinstance(_i, np.ndarray):
                    print(_i)
                    for _v in _i:
                        _l.append(_v)
                else:
                    _l += _i
        else:
            _l = _x
        _mean = self.mean(_l)
        _numerator = 0
        _denominator = len(_l)
        for _i in _l:
            _numerator += (_i - _mean) ** 2

        _t = _numerator / _denominator
        return _t

    def std(self, _x):
        """_summary_

        Args:
            _x (_type_): _description_
        """
        return self.var(_x) ** 0.5

if  __name__ == "__main__":
    n = np.ndarray(shape=(3,3), buffer=np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]), dtype=float)
    a = [1, 42, 300, 10, 59]
    tiny = TinyStatistician()
    print(tiny.std(a))
