from sample_project import code


def test_string_calculator_return_zero_empty_string():
    test_case = code.StringCalculator(0)
    assert test_case.add("") == 0


def test_string_calculator_return_number():
    test_case = code.StringCalculator(0)
    assert test_case.add("1") == 1
    assert test_case.add("2") == 2
    assert test_case.add("8") == 8


def test_string_calc_return_sum_of_two_numbers():
    test_case = code.StringCalculator(0)
    assert test_case.add("8,0") == 8
    assert test_case.add("1,4") == 5
    assert test_case.add("8,9") == 17
    assert test_case.add("3,1") == 4


"""
Allow the add() method to handle an unknown amount of numbers
"""


def test_str_calc_return_sum_of_multiple_numbers():
    test_case = code.StringCalculator(0)
    assert test_case.add("8,0,0") == 8
    assert test_case.add("8,10,2") == 20
    assert test_case.add("1,1,2") == 4
    assert test_case.add("9,1,4") == 14
    assert test_case.add("3,10,9") == 22
    assert test_case.add("10,100,1") == 111


"""
Allow the add() method to handle "\n"
"""


def test_str_calc_new_line_add():
    test_case = code.StringCalculator(0)
    assert test_case.add("1,2\n1") == 4
    assert test_case.add("4,3\n8") == 15
    assert test_case.add("6\n5,9,6,8") == 34


"""
Allow custom delimiters.
ex.
`"//;\n1;2"==3`
//l     delimiter pattern
\n      start numbers
1;2     delimiter
"""


def test_str_calc_provided_delimiter():
    test_case = code.StringCalculator(0)
    assert test_case.add("//;\n1;2") == 3
    assert test_case.add("//.\n4.2") == 6
    assert test_case.add("//;\n1;8,3") == 12
    assert test_case.add("\n1;2") == 3


def test_str_calc_no_negative_values_throw_exception():
    test_case = code.StringCalculator(0)
    assert test_case.add("11;-2") == 11
    assert test_case.add("-11;-2") == 0


def test_add_counter_by_one():
    test_code = code.StringCalculator(0)
    test_code.add("-11;-2")
    assert test_code.count == 1
    test_code.add("4,3")
    assert test_code.count == 2


def test_values_limited_to_1000():
    test_code = code.StringCalculator(0)
    assert test_code.add("1001,0") == 0
    assert test_code.add("1000,0") == 1000
