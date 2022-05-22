PYTHON_BIN ?= python

format: isort black

black:
	'$(PYTHON_BIN)' -m black --target-version py38 --exclude '/(\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|_build|buck-out|build|dist|node_modules|webpack_bundles)/' .

isort:
	'$(PYTHON_BIN)' -m isort home
	'$(PYTHON_BIN)' -m isort cv

venv:
	'$(PYTHON_BIN)' -m pip install -r requirements.txt

upgrade-venv:
	'$(PYTHON_BIN)' -m piptools compile -U requirements.in