# Scikitlearn packages
# Prep
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler

import pandas as pd
import numpy as np

# Models
from sklearn.ensemble import RandomForestClassifier

#Hyperparameter tuning packages
from sklearn.model_selection import GridSearchCV

#Metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

# Read in data 
import os
data_dir = os.path.dirname(os.getcwd()) + "/datasets"
import pickle

state_seed = 42
file_list = ["xtrain.pkl", "xtest.pkl", "ytrain.pkl", "ytest.pkl"]

for x in file_list:
    x = data_dir + "/" + x
    with open(x, 'rb') as file_in:
        if "xtrain" in x:
            X_train = pickle.load(file_in)
            file_in.close()
        if "xtest" in x:
            X_test = pickle.load(file_in)
            file_in.close()
        if "ytrain" in x:
            y_train = pickle.load(file_in)
            file_in.close()
        if "ytest" in x:
            y_test = pickle.load(file_in)
            file_in.close()

print(X_train.shape,X_test.shape, y_train.shape, y_test.shape)

#Create the model object
rf_class = RandomForestClassifier(
n_estimators=268
criterion='entropy'
    max_features= None,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=2,
)

#Fit to our model
rf_class.fit(X_train, y_train.values.ravel())

#Predict
y_test = pd.DataFrame(y_test) #This will avoide the setwithcopy warning, though not really necessary
y_test.loc[:,"predictions"] = rf_class.predict(X_test)

#Get confusion matrix 
print("Confustion Matrix \n", confusion_matrix(y_test.qualitary_binary, y_test.predictions))

