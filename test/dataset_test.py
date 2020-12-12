from mlmark.datasets import MNIST, FMNIST, OLIVETTI


class TestDatasets:
    def test_mnist(self):
        x = MNIST()
        assert len(x) > 0

    def test_fmnist(self):
        x = FMNIST()
        assert len(x) > 0

    def test_olivetti(self):
        x = OLIVETTI()
        assert len(x) > 0
