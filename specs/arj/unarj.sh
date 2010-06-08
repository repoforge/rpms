#!/bin/sh

set -e

if [ $# -eq 1 ]; then
  arj l "$@"
else
  arj "$@"
fi

