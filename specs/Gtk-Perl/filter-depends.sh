#!/bin/sh

/usr/lib/rpm/find-requires.perl $* | grep -v HTTP::GHTTP | grep -v OpenGL | grep -v XML::Writer
