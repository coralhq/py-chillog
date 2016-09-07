SHELL := bash

IMAGE = coralteam/py-chillog
VERSION ?= latest
TEST_PREFIX ?= test-

RESULT_DIR = ${PWD}/test-results
test_dir = tests
result_name = results.xml
coverage_name = coverage.xml

.PHONY: build push test integration-test  \
	clean img-clean

test: test-clean unit-test

clean: test-clean

install:
	python setup.py install

unit-test:
	mkdir -p ${RESULT_DIR}

	# install dependency
	pip install -r requirements.txt --upgrade

	# run unit test
	set -e

	(cd ${test_dir} && nosetests --stop \
	    --config=.noserc \
	    --with-xunit --with-xcoverage \
	    --xunit-file=${RESULT_DIR}/${result_name} \
	    --xcoverage-file=${RESULT_DIR}/${coverage_name})

test-clean:
	# clean test result folder
	rm -rf ${PWD}/test-results
