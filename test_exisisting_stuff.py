
import math

#test sum(numbers: List[float]) -> float

#def test_sum():
  #  some_list = [1,2,3]
   # assert sum(some_list) == 6

def test_sum():
    assert sum([]) == 0
    assert sum([1,2,3]) == 6
    assert sum([5,5,5]) == 15
    assert sum([1]*1000) == 1000

#test math.floor(float) -> int
def test_math_ceil():
    assert math.ceil(6.0001) == 7
    assert math.ceil(6.0) == 6
    assert math.ceil(6.9999) == 7

def test_math_floor():
    assert math.floor(6.001) == 6
    assert math.floor(5.999) == 5
    assert math.floor(6.0) == 6
  
def test_f_strings():
  assert f"hello {3 + 5}" == "hello 8"

a, b = 3, 4
assert f"result: {a+b}" == "result: 7"

def test_dot_format():
  assert "{} {} {}".format(1,2,3) == "1 2 3"
  assert "blah {} blah".format("happy") == "blah happy blah"