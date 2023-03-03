import numpy as np

def model_test(testing_set, slope, intercept):
    dim = testing_set.ndim
    if dim != 2:
        raise ValueError("Argument testing_set must be two dimensional. Got {0} dimensional array instead!".format(dim))
    num_cols = testing_set.shape[1]
    if num_cols != 2:
        raise ValueError("Argument testing_set must have 2 columns for univariate linear regression. "
                            "It actually has {0} columns".format(num_cols)
                            )
    actual_price = testing_set[:, 1]
    predicted_price = slope*testing_set[:, 0] + intercept
    residual_sum_of_squares = np.sum(np.square(predicted_price - actual_price)) / testing_set.shape[0]
    return 1 - residual_sum_of_squares / np.var(actual_price)
