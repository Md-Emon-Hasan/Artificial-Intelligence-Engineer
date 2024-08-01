import bentoml
import numpy as np
from bentoml.io import NumpyNdarray

clf = bentoml.sklearn.get('kneighbors:latest').to_runner()

service = bentoml.Service(
    'kneighbors',runners=[clf]
)

# create an API function
@service.api(input=NumpyNdarray(),output=NumpyNdarray())
def predict(input_series: np.ndarray) -> np.ndarray:
    result = clf.predict.run(input_series)
    return result