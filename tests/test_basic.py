from sample_project import code


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
Allow the add() method to handle an unknown amount of numbers
"""


def test_str_calc_return_sum_of_multiple_numbers():
    assert code.StringCalculator.add("8,0,0") == 8
    assert code.StringCalculator.add("8,10,2") == 20
    assert code.StringCalculator.add("1,1,2") == 4
    assert code.StringCalculator.add("9,1,4") == 14
    assert code.StringCalculator.add("3,10,9") == 22
    assert code.StringCalculator.add("10,100,1") == 111


"""
Allow the add() method to handle "\n"
"""


def test_str_calc_new_line_add():
    assert code.StringCalculator.add("1,2\n1") == 4
    assert code.StringCalculator.add("4,3\n8") == 15
    assert code.StringCalculator.add("6\n5,9,6,8") == 34


"""
Allow custom delimiters.
ex.
`"//;\n1;2"==3`
//l     delimiter pattern
\n      start numbers
1;2     delimiter
"""


def test_str_calc_provided_delimiter():
    assert code.StringCalculator.add("//;\n1;2") == 3
    assert code.StringCalculator.add("//.\n4.2") == 6
    assert code.StringCalculator.add("//;\n1;8,3") == 12
    assert code.StringCalculator.add("\n1;2") == 3


def test_str_calc_no_negative_values_throw_exception():
    assert code.StringCalculator.add("11;-2") == 11
