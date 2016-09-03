#!/bin/bash

set -e

# clean
RESULT_DIR=${PWD}"/test-results"
echo ${RESULT_DIR}
test_dir=tests
result_name=results.xml
coverage_name=coverage.xml

# test
(cd ${test_dir} && nosetests --stop \
  --config=.noserc \
  --with-xunit --with-xcoverage \
  --xunit-file=${RESULT_DIR}/${result_name} \
  --xcoverage-file=${RESULT_DIR}/${coverage_name})
