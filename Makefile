all:
	echo use targets env or tests

env:
	test -d env || virtualenv env
	env/bin/pip install -r requirements.txt

tests:
	python -m unittest discover -s src

.PHONY: env
