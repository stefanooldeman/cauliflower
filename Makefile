clean-pyc:
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

pep8:
	pep8 --show-pep8 -r discolib && echo "All good!"

unittest: clean-pyc
	coverage erase
	SETTINGS_PATH='.' coverage run --include "discolib*" --omit "*test*" -m unittest2 discover
	coverage report
	coverage html -d docs/coverage/

test: pep8 unittest
