import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# load the csv file
# df = pd.read_csv('iris.csv')
df = pd.read_csv('C:/Users/emon1/OneDrive/Desktop/AI Engineer/Flask/Deploy Machine Learning Model Flask/iris.csv')

print(df.head())

# select independent and dependent variable
x = df[['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']]
y = df['Class']

# split the dataset into train and test
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=26)

# Feature scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(x_train,y_train)

# Make pickle file of our model
pickle.dump(classifier,open('model.pkl','wb'))
