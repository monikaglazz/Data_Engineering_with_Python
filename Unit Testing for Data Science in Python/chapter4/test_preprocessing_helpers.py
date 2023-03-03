import pytest
import unittest.mock.call
from preprocessing_helpers import raw_and_clean_data_file, convert_to_int


class TestPreprocess(object):
    # Define a function convert_to_int_bug_free
    def convert_to_int_bug_free(self, comma_separated_integer_string):
        # Assign to the dictionary holding the correct return values
        return_values = {"1,801": 1801, "201,411": 201411, "2,002": 2002,
                         "333,209": 333209, "1990": None, "782,911": 782911, "1,285": 1285, "389129": None}
        # Return the correct result using the dictionary return_values
        return return_values[comma_separated_integer_string]


    # Add the correct argument to use the mocking fixture in this test
    def test_on_raw_data(self, raw_and_clean_data_file, mocker):
        raw_path, clean_path = raw_and_clean_data_file
        # Replace the dependency with the bug-free mock
        convert_to_int_mock = mocker.patch("data.preprocessing_helpers.convert_to_int",
                                           side_effect=convert_to_int_bug_free)
        preprocess(raw_path, clean_path)
        # Check if preprocess() called the dependency correctly
        assert convert_to_int_mock.call_args_list == [call("1,801"), call("201,411"), call(
            "2,002"), call("333,209"), call("1990"), call("782,911"), call("1,285"), call("389129")]
        with open(clean_path, "r") as f:
            lines = f.readlines()
        first_line = lines[0]
        assert first_line == "1801\\t201411\\n"
        second_line = lines[1]
        assert second_line == "2002\\t333209\\n"

