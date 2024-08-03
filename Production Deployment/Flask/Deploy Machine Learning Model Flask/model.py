# Imorting denpendencicy
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the iris dataset
iris = load_iris()

# target the data
x = iris.data
y = iris.target

# split the data
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# train the data in RandomForestClassifier Algorithm
model = RandomForestClassifier(n_estimators=100,random_state=42)

# fit the model
model.fit(x_train,y_train)

# save the trained model to a file
joblib.dump(model,'iris_model.pkl')
