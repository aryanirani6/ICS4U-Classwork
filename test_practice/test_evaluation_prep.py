import evaluation_prep

def test_add():
    assert evaluation_prep.add(1,1) == 2

def test_sum_list():
    assert evaluation_prep.sum_list([1,2,3,4,5]) == 15

