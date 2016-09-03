#!/bin/bash

case $1 in
  "unit")
    ./test-unit.sh
    ;;
  *)
    echo "usage: $0 [unit]"
    exit 1
    ;;
esac