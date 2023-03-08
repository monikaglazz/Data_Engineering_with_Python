from pyspark.ml.classification import LogisticRegression
import pyspark.ml.evaluation as evals
import pyspark.ml.tuning as tune
import numpy as np
from chapter3 import training, test


# ex 1 "Create a LogicRegression estimator"
lr = LogisticRegression()


# ex 2 "Create a BinaryClassificationEvaluator"
evaluator = evals.BinaryClassificationEvaluator(metricName="areaUnderROC")


# ex 3 "Create a grid of values to search over when looking for the optimal hyperparameters"
grid = tune.ParamGridBuilder()

# Add the hyperparameter
grid = grid.addGrid(lr.regParam, np.arange(0, .1, .01))
grid = grid.addGrid(lr.elasticNetParam, [0, 1])

# Build the grid
grid = grid.build()


# ex 4 "Create CrossValidator for cross validation"
cv = tune.CrossValidator(estimator=lr,
                         estimatorParamMaps=grid,
                         evaluator=evaluator
                         )


# ex 5 "Fit the models"
# Fit cross validation models
models = cv.fit(training)

# Extract the best model
best_lr = models.bestModel


# ex 6 "Evaluate the model"
# Use the model to predict the test set
test_results = best_lr.transform(test)

# Evaluate the predictions
print(evaluator.evaluate(test_results))
