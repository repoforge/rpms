#!/bin/bash

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
now=$(date +%Y%m%d)

cd "$tmp"
hg clone http://linuxtv.org/hg/dvb-apps
cd dvb-apps
tar jcf "$pwd"/dvb-apps-tuningfiles-$now.tar.bz2 util/scan/{atsc,dvb-?}
cd ..
cd - >/dev/null
