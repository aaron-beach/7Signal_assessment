from sample_project import code


def test_hello():
    assert code.greeting() != ""
    assert code.greeting() == "Hello, World!"


def test_string_calculator_return_zero_empty_string():
    assert code.StringCalculator.add("") == 0
