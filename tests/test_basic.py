from sample_project import code


def test_hello():
    assert code.greeting() != ""
    assert code.greeting() == "Hello, World!"
