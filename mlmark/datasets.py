from sklearn.datasets import load_digits, fetch_openml, fetch_olivetti_faces

MNIST = load_digits
FMNIST = lambda: fetch_openml(name="Fashion-MNIST")
OLIVETTI = fetch_olivetti_faces
