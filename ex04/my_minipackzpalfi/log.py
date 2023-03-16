"""_summary_

Returns:
    _type_: _description_
"""

import time
from random import randint

_f = open("machine.log", 'w')

def log(func):
    """_summary_

    Args:
        func (_type_): _description_
    """
    def wrapper(*args, **kwargs):
        prev = time.time()
        result = func(*args, **kwargs)
        new = time.time()
        _t = new - prev
        if _t < 0.001:
            _t *= 100
            _ts = "ms"
        else:
            _ts = "s"
        _f.write("(cmaxime)Running: {:<19}[ exec-time = {:.3f} {}]\n".format( \
            str(func.__name__).replace("_", " ").capitalize(), \
            _t,
            _ts
            ))
        return  result
    return wrapper

class CoffeeMachine():
    """_summary_

    Returns:
        _type_: _description_
    """

    water_level = 100

    @log
    def start_machine(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "boiling..."

    @log
    def make_coffee(self):
        """_summary_
        """
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        """_summary_

        Args:
            water_level (_type_): _description_
        """
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
