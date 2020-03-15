from sample_project import code


def test_hello():
    assert code.greeting() != ""
    assert code.greeting() == "Hello, World!"


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
