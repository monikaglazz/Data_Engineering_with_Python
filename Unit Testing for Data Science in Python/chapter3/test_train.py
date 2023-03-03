import pytest
import numpy as np
from train import split_into_training_and_testing_sets


# Declare the test class
class TestSplitIntoTrainingAndTestingSets(object):
    # Fill in with the correct mandatory argument
    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        assert exc_info.match(expected_error_msg)


# in the command line to run file:
# pytest test_train.py

# in the command line to run only class:
# pytest test_train.py::TestSplitIntoTrainingAndTestingSets

# in the command line to run one test from class:
# pytest test_train.py::TestSplitIntoTrainingAndTestingSets::test_on_one_row


# Expected failure test for model_test
@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(
            test_input, expected, actual)
        assert actual == pytest.approx(expected), message

    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)


# in the command line to run file:
# pytest test_train.py

# in the command line to run only class:
# pytest test_train.py::TestModelTest

# in the command line to run one test from class:
# pytest test_train.py::TestModelTest::test_on_linear_data
