import pytest
from preprocessing_helpers import convert_to_int

# 1st and 3rd functions are the same but made in 2 different ways just for practice


def test_on_string_with_one_comma():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(
        actual)
    assert actual == expected, message


def test_with_no_comma():
    actual = convert_to_int("756")
    assert actual == 756, "Expected: 756, Actual: {0}".format(actual)


def test_with_one_comma():
    actual = convert_to_int("2,081")
    assert actual == 2081, "Expected: 2081, Actual: {0}".format(actual)


def test_with_two_commas():
    actual = convert_to_int("1,034,891")
    assert actual == 1034891, "Expected: 1034891, Actual: {0}".format(actual)


def test_on_string_with_missing_comma():
    actual = convert_to_int("178100,301")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_string_with_incorrectly_placed_comma():
    actual = convert_to_int("12,72,891")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_float_valued_string():
    actual = convert_to_int("23,816.92")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


# in command line:
# pytest test_convert_to_int.py
