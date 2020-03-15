from sample_project import code


"""
   2. Start with the **simplest** test case of an **empty string** and move to **one & two numbers**
"""


def test_string_calculator_return_zero_empty_string():
    assert code.StringCalculator.add("") == 0


def test_string_calculator_return_number():
    assert code.StringCalculator.add("1") == 1
    assert code.StringCalculator.add("2") == 2
    assert code.StringCalculator.add("8") == 8


def test_string_calc_return_sum_of_two_numbers():
    assert code.StringCalculator.add("8,0") == 8
    assert code.StringCalculator.add("1,4") == 5
    assert code.StringCalculator.add("8,9") == 17
    assert code.StringCalculator.add("3,1") == 4


"""
2. Allow the **Add** method to handle an unknown amount of numbers
"""


def test_str_calc_return_sum_of_multiple_numbers():
    assert code.StringCalculator.add("8,0,0") == 8
    assert code.StringCalculator.add("8,10,2") == 20
    assert code.StringCalculator.add("1,1,2") == 4
    assert code.StringCalculator.add("9,1,4") == 14
    assert code.StringCalculator.add("3,10,9") == 22
    assert code.StringCalculator.add("10,100,1") == 111


def test_str_calc_new_line_add():
    assert code.StringCalculator.add("1:2\n1") == 4
