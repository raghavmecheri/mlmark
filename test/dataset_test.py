from mlmark.datasets import MNIST, FMNIST, OLIVETTI


class TestDatasets:
    def test_mnist(self):
        x = MNIST["fetch"]()
        assert len(x) > 0

    def test_fmnist(self):
        x = FMNIST["fetch"]()
        assert len(x) > 0

    def test_olivetti(self):
        x = OLIVETTI["fetch"]()
        assert len(x) > 0
