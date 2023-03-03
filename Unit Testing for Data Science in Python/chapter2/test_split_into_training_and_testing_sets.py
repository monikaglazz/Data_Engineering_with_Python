from models import split_into_training_and_testing_sets
import numpy as np
import pytest


def test_on_six_rows():
    example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                 [1148.0, 206186.0], [1506.0, 248419.0],
                                 [1210.0, 214114.0], [1697.0, 277794.0]]
                                )
    # training array's expected number of rows
    expected_training_array_num_rows = int(0.75*(len(example_argument)))
    # testing array's expected number of rows
    expected_testing_array_num_rows = round(
        len(example_argument) - int(0.75*len(example_argument)))
    actual = split_into_training_and_testing_sets(example_argument)
    # Write the assert statement checking training array's number of rows
    assert actual[0].shape[0] == expected_training_array_num_rows, "The actual number of rows in the training array is not {}".format(
        expected_training_array_num_rows)
    # Write the assert statement checking testing array's number of rows
    assert actual[1].shape[0] == expected_testing_array_num_rows, "The actual number of rows in the testing array is not {}".format(
        expected_testing_array_num_rows)


def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    # Store information about raised ValueError in exc_info
    with pytest.raises(ValueError) as exc_info:
        split_into_training_and_testing_sets(test_argument)
    expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
    # Check if the raised ValueError contains the correct message
    assert exc_info.match(expected_error_msg)

# in the command line:
# pytest test_split_into_training_and_testing_sets.py
