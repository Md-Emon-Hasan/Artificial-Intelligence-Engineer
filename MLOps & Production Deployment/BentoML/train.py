import bentoml

from sklearn import svm
from sklearn import datasets

# load training data set
iris = datasets.load_iris()

X = iris.data
y = iris.target

# train the model
clf = svm.SVC(gamma='scale')
clf.fit(X,y)

# Save model to the Bento local model store
saved_model = bentoml.sklearn.save_model('iris_clf',clf)
print(f'Model saved: {saved_model}')

# step 1
# file ti run korte hobe, run korle nicher line er moto ekti code pawa jabe
## iris_clf:4nxboh2m36k5mlh5

# step 2
# "bentoml models list" eita run command e likhle bentoml ei sob model er list dekha jabe