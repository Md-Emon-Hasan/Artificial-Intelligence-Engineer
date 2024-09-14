import click
import streamlit as st
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

st.title('Stramlit Example')
st.write('''
# Explore different classifier
Which one is the best?         
''')

dataset_name = st.sidebar.selectbox('Select Dataset',('Iris','Breast Cancer','Wine Dataset'))
st.write(dataset_name)

classifier_name = st.sidebar.selectbox('Selcet Classifer',('KNN','SVM','Random Forest'))

def get_datasets(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == 'Breast Cancer':
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    
    x = data.data
    y = data.target
    return x,y
        
x,y = get_datasets(dataset_name)
st.write("shape of dataset",x.shape)
st.write('Number of classes',len(np.unique(y)))

def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == 'SVM':
        C = st.sidebar.slider('C', 0.01, 10.0)
        params['C'] = C
    elif clf_name == 'KNN':
        K = st.sidebar.slider('K', 1, 15)
        params['K'] = K
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 15)
        params['max_depth'] = max_depth
        n_estimators = st.sidebar.slider('n_estimators', 1, 100)
        params['n_estimators'] = n_estimators
    return params

params = add_parameter_ui(classifier_name)

def get_classifier(clf_name, params):
    clf = None
    if clf_name == 'SVM':
        clf = SVC(C=params['C'])
    elif clf_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        clf = clf = RandomForestClassifier(n_estimators=params['n_estimators'], max_depth=params['max_depth'], random_state=2)
    return clf

clf = get_classifier(classifier_name, params)

# classification
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=1234,stratify=y)

clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

acc = accuracy_score(y_test,y_pred)

st.write(f'classifier = {classifier_name}')
st.write(f'Accuracy = {acc}')

# PLOT
pca = PCA(2)
x_projected = pca.fit_transform(x)

x1 = x_projected[:,0]
x2 = x_projected[:,1]

fig = plt.figure()
plt.scatter(x1,x2,c=y,alpha=0.8,cmap='viridis')
plt.xlabel('Principle Component 1')
plt.ylabel('Principle Component 2')
plt.colorbar()

# plt show
st.pyplot(fig)