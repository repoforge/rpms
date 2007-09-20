#!/bin/sh
# Wrapper script for lmbench

if [ $(id -u) -gt 0 ]; then
    echo "You must run this as the root user"
    exit 0
fi

cd /usr/lib/lmbench/results
if [ -n "$1" -a -x ../scripts/${1} ]; then
    exec ../scripts/$@
else
    CONFIG=`../scripts/config`
    OS=`../scripts/os`
    [ -f "../bin/$OS/$CONFIG" ] || ../scripts/config-run
    ../scripts/results
fi
cd - >/dev/null
exit 0
