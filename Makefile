install:
	python3 -m pip install --upgrade pip
	pip install -r requirements.txt

freeze: FORCE
	pip freeze > requirements.txt

test: FORCE
	export PYTHONPATH=$(PWD)
	python -m pytest

FORCE: