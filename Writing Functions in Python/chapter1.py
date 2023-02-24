import inspect
import pandas as pd

# 1 "Google format docstring"


def count_letter(content, letter):
    """Count the number of times `letter` appears in `content`.

    Args:
      content (str): The string to search.
      letter (str): The letter to search for.

    Returns:
      int

    Raises:
      ValueError: If `letter` is not a one-character string.
    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')
    return len([char for char in content if char == letter])

# 2 "Retrieving docstrings"


def build_tooltip(function):
    """Create a tooltip for any function that shows the
    function's docstring.

    Args:
      function (callable): The function we want a tooltip for.

    Returns:
      str
    """
    # Get the docstring for the "function" argument by using inspect
    docstring = inspect.getdoc(function)
    border = '#' * 28
    return '{}\n{}\n{}'.format(border, docstring, border)


print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))

# 3

gp_list = [[2.7858767423914466, 2.0525126167960086, 2.170543703154024, 0.06556992350372548],
           [1.1445573398015179, 2.6664982006562865,
               0.2670977729000188, 2.884737464202427],
           [0.9074058142568124, 0.4236339402272553,
               2.6134594854121627, 0.03095005650361582],
           [2.205259076331565, 0.523579802656323,
               3.9843453094713017, 0.3392891097809345],
           [2.87787587914225231, 0.2879224258732322,
               3.077589348295849, 0.9019936418000944],
           [1.6924258404978438, 2.646257346664975,
               2.295096454635298, 3.5004981354928986],
           [3.923056793538462, 3.3860249010828882,
               0.41054103684318344, 1.4543052719504534],
           [2.739318954339453, 2.2130293791868536,
               2.799336299091659, 2.159839740850234],
           [1.9237276059374437, 3.417809950098019,
               2.6446714693117244, 2.2724128552759137],
           [1.568470072776602, 1.5393512451030444, 0.19638852249110528, 0.9018534412238397]]

df = pd.DataFrame(gp_list, columns=['y1_gpa', 'y2_gpa', 'y3_gpa', 'y4_gpa'])


def standardize(column):
    """Standardize the values in a column.

    Args:
      column (pandas Series): The data to standardize.

    Returns:
      pandas Series: the values as z-scores
    """
    # Finish the function so that it returns the z-scores
    z_score = (column - column.mean()) / column.std()
    return z_score


# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df.y1_gpa)
df['y2_z'] = standardize(df.y2_gpa)
df['y3_z'] = standardize(df.y3_gpa)
df['y4_z'] = standardize(df.y4_gpa)

# 4


def mean(values):
    """Get the mean of a sorted list of values

    Args:
      values (iterable of float): A list of numbers

    Returns:
      float
    """
    # Write the mean() function
    mean = sum(values) / len(values)
    return mean


def median(values):
    """Get the median of a sorted list of values

    Args:
      values (iterable of float): A list of numbers

    Returns:
      float
    """
    # Write the median() function
    midpoint = int(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]
    return median

# 5

# Use an immutable variable for the default argument


def better_add_column(values, df=None):
    """Add a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.

    Args:
      values (iterable): The values of the new column
      df (DataFrame, optional): The DataFrame to update.
        If no DataFrame is passed, one is created by default.

    Returns:
      DataFrame
    """
    # Update the function to create a default DataFrame
    if df is None:
        df = pd.DataFrame()
    df['col_{}'.format(len(df.columns))] = values
    return df
