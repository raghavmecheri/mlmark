class Supervised:
    def __init__(self):
        pass

    def fit(self, x, y):
        raise NotImplementedError(
            "Supervised is meant to serve only as an abstract class for a supervised learning model. Please implement your own subclass, with its own fit(self, x, y) call"
        )

    def transform(self, x):
        raise NotImplementedError(
            "Supervised is meant to serve only as an abstract class. Please implement your own subclass, with its own transform(self, x) call"
        )


class Unsupervised:
    def __init__(self):
        pass

    def fit(self, x):
        raise NotImplementedError(
            "Unsupervised is meant to serve only as an abstract class for an unsupervised learning model. Please implement your own subclass, with its own fit(self, x) call"
        )

    def transform(self, x):
        raise NotImplementedError(
            "Unsupervised is meant to serve only as an abstract class for an unsupervised learning model. Please implement your own subclass, with its own transform(self, x) call"
        )
