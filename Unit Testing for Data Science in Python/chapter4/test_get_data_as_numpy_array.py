from chapter3.as_numpy import get_data_as_numpy_array
import numpy as np
import pytest
import os


# fixture and test for an clean data file
# Add a decorator to make this function a fixture
@pytest.fixture
def clean_data_file():
    file_path = "clean_data_file.txt"
    with open(file_path, "w") as f:
        f.write("201\t305671\n7892\t298140\n501\t738293\n")
    yield file_path
    os.remove(file_path)


def test_on_clean_file(clean_data_file):
    expected = np.array(
        [[201.0, 305671.0], [7892.0, 298140.0], [501.0, 738293.0]])
    actual = get_data_as_numpy_array(clean_data_file, 2)
    assert actual == pytest.approx(
        expected), "Expected: {0}, Actual: {1}".format(expected, actual)


# fixture and test for an empty data file
# Add a decorator to make this function a fixture
@pytest.fixture
def empty_file():
    file_path = "empty.txt"
    open(file_path, "w").close()
    yield file_path
    os.remove(file_path)


def test_on_empty_file(self, empty_file):
    expected = np.empty((0, 2))
    actual = get_data_as_numpy_array(empty_file, 2)
    assert actual == pytest.approx(
        expected), "Expected: {0}, Actual: {1}".format(expected, actual)


# 
# Fixture chaining using tmpdir
@pytest.fixture
def empty_file(tmpdir):
    file_path = tmpdir.join("empty.txt")
    open(file_path, "w").close()
    yield file_path