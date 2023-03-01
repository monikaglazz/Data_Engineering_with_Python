#Scikitlearn packages
#Prep
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler

#Models
from sklearn.linear_model import LogisticRegression

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

#Create the model object, setting C manually
log_reg = LogisticRegression(penalty='l2', 
dual=False,
C=0.1,
fit_intercept=False,
class_weight='balanced',
random_state=state_seed,
solver='liblinear'
max_iter=292
multi_class='ovr',
verbose=1,
n_jobs=4)

#Fit to our model
log_reg.fit(X_train, y_train.values.ravel())

# Get results
# Predict the class
y_test = pd.DataFrame(y_test) #This will avoide the setwithcopy warning, though not really necessary
y_test["predictions"] = log_reg.predict(X_test)

# Get confusion matrix 
print("Confustion Matrix \n", confusion_matrix(y_test.qualitary_binary, y_test.predictions))

