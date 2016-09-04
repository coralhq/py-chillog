SHELL := bash

IMAGE = coralteam/py-chillog
VERSION ?= latest
TEST_PREFIX ?= test-

.PHONY: build push test integration-test  \
	clean img-clean

build:
	docker build -f docker/Dockerfile -t "$(IMAGE):$(VERSION)" .

test: test-clean unit-test

clean: test-clean

install:
	python setup.py install

test_version.txt:
	# put version tag for test image into a test_version.txt
	# e.g. test-ab12cd34
	echo -n "$(TEST_PREFIX)" > test_version.txt
	cat /dev/urandom | LC_CTYPE=C tr -dc 'a-f0-9' | fold -w 8 | head -n 1 \
		>> test_version.txt

unit-test: test_version.txt
	$(MAKE) -e VERSION=$$(cat test_version.txt) build
	mkdir -p test-results
	docker run --rm -v $$(pwd)/test-results:/app/test-results \
			$(IMAGE):$$(cat test_version.txt) unit

test-clean:
	# clean test result folder
	rm -rf ${PWD}"/test-results"

img-clean:
	# clean images
	docker rmi $(IMAGE):$(VERSION) || true
