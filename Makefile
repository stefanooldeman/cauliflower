clean-pyc:
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

pep8:
	pep8 -r cauliflower && echo "All good!"

unittest: clean-pyc
	coverage erase
	SETTINGS_PATH='.' coverage run --include "cauliflower*" --omit "*test*" -m unittest discover
	coverage report
	coverage html -d docs/coverage/

test: pep8 unittest
