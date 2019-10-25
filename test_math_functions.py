#to import from other files, just say this

import math_functions as m

def test_add():
    assert m.add(1,1) == 2
    assert m.add(3,6) == 9

def test_subtract():
    assert m.subtract(5,2) == 3