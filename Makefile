.PHONY: build test docs lint clean

build:
	maturin develop

test:
	pytest

docs:
	cd docs && make html

lint:
	black .
	ruff check .

fmt:
	black .
	ruff check . --fix

clean:
	rm -rf target/
	rm -rf docs/_build/
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete