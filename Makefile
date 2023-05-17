check-linting:
	poetry run isort --check --profile black meetings/ tests/ examples/
	poetry run flake8 --exit-zero meetings/ tests/ --exit-zero
	poetry run black --check --diff meetings/ tests/ --line-length 119


fix-linting:
	poetry run isort --profile black meetings/ tests/
	poetry run black meetings/ tests/ --line-length 119


test:
	poetry run pytest -v