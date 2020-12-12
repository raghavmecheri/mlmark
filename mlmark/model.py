class Model:
    def __init__(self):
        pass

    def fit(self, data):
        raise NotImplementedError(
            "Model is meant to serve only as an abstract class. Please implement your own subclass, with its own fit(self, data) call"
        )

    def transform(self, data):
        raise NotImplementedError(
            "Model is meant to serve only as an abstract class. Please implement your own subclass, with its own transform(self, data) call"
        )
