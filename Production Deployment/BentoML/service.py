from unittest import result
import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

# Define the input data structure
iris_clf_runner = bentoml.sklearn.get('iris_clf:latest').to_runner()

svc = bentoml.Service('iris_classifier',runners=[iris_clf_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_seris: np.ndarray) -> np.ndarray:
    result = iris_clf_runner.predict.run(input_seris)
    return result

# step 1
# file ti run korte hobe

# step 2
# "bentoml serve service.py:svc --reload" ei command ti likhe run korte hobe, eita run korle ekta API pawa jabe seitate click korte hobe