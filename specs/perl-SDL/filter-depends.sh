#!/bin/sh

/usr/lib/rpm/find-requires.perl $* | grep -v Pod::ToDemo
