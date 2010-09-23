#!/bin/bash

if [ $# -gt 0 ]; then  
  DATE=$1
  shift
else
  DATE=$(date +%Y%m%d)
fi

MODULE="$(basename $0 -cvs_checkout.sh)"

set -x
rm -rf $MODULE

cvs -z3 -d:pserver:anonymous@tidy.cvs.sourceforge.net:/cvsroot/tidy export -D $DATE $MODULE 

## tar it up
tar czf $MODULE-${DATE}cvs.tar.gz $MODULE

## cleanup
rm -rf $MODULE

