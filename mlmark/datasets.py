from sklearn.datasets import load_digits, fetch_openml, fetch_olivetti_faces

MNIST = {"name": "MNIST", "fetch": load_digits}

FMNIST = {
    "name": "Fashion MNIST",
    "fetch": lambda: fetch_openml(name="Fashion-MNIST"),
}

OLIVETTI = {"name": "Olivetti Faces", "fetch": fetch_olivetti_faces}
