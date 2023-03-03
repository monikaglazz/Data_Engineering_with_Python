import pytest
from preprocessing_helpers import row_to_list


def test_on_no_tab_no_missing_value():
    actual = row_to_list("123\n")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_two_tabs_no_missing_value():
    actual = row_to_list("123\t4,567\t89\n")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_one_tab_with_missing_value():
    actual = row_to_list("\t4,567\n")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_no_tab_with_missing_value():
    actual = row_to_list("\n")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_two_tabs_with_missing_value():
    actual = row_to_list("123\t\t89\n")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_normal_argument_1():
    actual = row_to_list("123\t4,567\n")
    expected = ["123", "4,567"]
    assert actual == expected, "Expected: {0}, Actual: {1}".format(
        expected, actual)


def test_on_normal_argument_2():
    actual = row_to_list("1,059\t186,606\n")
    expected = ["1,059", "186,606"]
    assert actual == expected, "Expected: {0}, Actual: {1}".format(
        expected, actual)

# in the command line:
# pytest test_row_to_list.py
