import time


def run(model, datasets, runs=10):
    results = {}
    fits, transforms = [], []
    for dataset in datasets:
        name, data = dataset["name"], dataset["fetch"]
        x = data()
        for i in range(runs):
            start_fit = time.process_time()
            model.fit(x)
            fits.append(time.process_time() - start_fit)
            start_transform = time.process_time()
            model.transform(x)
            transforms.append(time.process_time() - start_transform)
        results[name] = {
            "fit": sum(fits) / len(fits),
            "transform": sum(transforms) / len(transforms),
        }
    return results
