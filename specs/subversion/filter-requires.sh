#!/bin/sh
# Munge Perl requirements:
# - remove dependency on Config::Inifiles
# - only require File::Path >= 1.04, not >= 1.404
/usr/lib/rpm/perl.req $* | 
sed -e '/perl(Config::IniFiles)/d' \
    -e 's/perl(File::Path) >= 1.0404/perl(File::Path) >= 1.04/'

    
