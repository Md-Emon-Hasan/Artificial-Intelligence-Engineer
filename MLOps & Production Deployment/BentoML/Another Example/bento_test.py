import bentoml

clf = bentoml.sklearn.get('kneighbors:latest').to_runner()

clf.init_local()

result = clf.predict.run([[2.4,1.4,3.5,4.6]])

print(result)