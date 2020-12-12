from mlmark.benchmark import run
from mlmark.model import Model
from mlmark.datasets import MNIST, FMNIST, OLIVETTI

import numpy as np


class MockModelClass(Model):
    def fit(self, data):
        self.model = None

    def transform(self, x):
        return np.ones(len(x))


model = MockModelClass()


class TestBenchmark:
    def test_benchmark(self):
        def _require_structure(results):
            for key, value in results.items():
                if "fit" not in value and "transform" not in value:
                    return False
            return True

        data = [MNIST, FMNIST, OLIVETTI]
        results = run(model, data)

        assert len(results.items()) == len(data)
        structure = _require_structure(results)
        assert structure is True
