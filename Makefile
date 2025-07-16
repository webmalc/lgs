.DEFAULT_GOAL := test_lint
.PHONY := test_lint lint test coverage test_parallel ruff mypy

mypy:
	mypy .
ruff:
	ruff check --output-format=concise

lint: ruff mypy

coverage:
	pytest --cov=./ --cov-report html
	${BROWSER} htmlcov/index.html

test:
	pytest --cov=./

test_parallel:
	pytest -n auto

test_lint: lint test