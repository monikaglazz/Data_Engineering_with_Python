import sys
import pytest
import numpy as np
from as_numpy import get_data_as_numpy_array


class TestGetDataAsNumpyArray(object):
    # Mark as skipped if Python version is greater than 2.7
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array(
            "example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(
            expected, actual)
        assert actual == pytest.approx(expected), message


# in the command line to run file:
# pytest test_as_numpy.py

# in the command line to run only class:
# pytest test_as_numpy.py::TestGetDataAsNumpyArray

# in the command line to run one test from class:
# pytest test_as_numpy.py::TestGetDataAsNumpyArray::test_on_clean_file

# to show the reason for expected failures in the test result report:
# pytest -rx

# to show the reason for skipped tests in the test result report:
# pytest -rs

# to show the reason for both skipped tests and tests that are expected to fail in the test result report
# pytest -rsx
