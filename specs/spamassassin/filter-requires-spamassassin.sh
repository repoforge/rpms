#!/bin/sh

/usr/lib/rpm/find-requires $* | grep -v 'perl(Net::SMTP::Server' | grep -v 'perl(MIME::Body'
