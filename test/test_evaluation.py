import evaluation

def test_average_marks():
    assert evaluation.average_marks(3,3,3) == 3

def test_number_occurences():
    initial_list = [10,20,20,5]
    expected_2 = [10:1, 20:2, 5:1]
    result = evaluation.number_occurences(initial_list)
    assert result == expected_2

def test_occurences_times():
    initial_list2 = [10,20,15,10,20]
    expected_3 = {10: 2, 20: 2, 15: 1}
    result = evaluation.occurences_times(initial_list2)
    assert result == expected_3
def test_reverse_occurence():
    initial_dict = {}
    expected_4 = []
    result = evaluation.reverse_occurences(initial_dict)
    assert result == expected_4
