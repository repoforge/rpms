# $Id$
# Authority: dag

%define real_version 0.1h

Summary: Guesses and recovers a damaged MBR (Master Boot Record)
Name: gpart
Version: 0.1
Release: 0.h
License: GPL
Group: Applications/System
URL: http://home.pages.de/~michab/gpart/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.stud.uni-hannover.de/user/76201/gpart/%{name}-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Gpart is a small tool which tries to guess what partitions are on a PC
type harddisk in case the primary partition table was damaged.

%prep
%setup -n %{name}-%{real_version}

### FIXME: Fix PPC build (Please fix upstream)
%{__perl} -pi.orig -e 's/(defined\(__alpha__\))/$1 || defined(__powerpc__)/g' src/gm_ntfs.h

### FIXME: Fix broken build on RH9 (Please fix upstream)
%{__perl} -pi.orig -e 's|(#include "l64seek.h")|$1\n#include <errno.h>|g' src/gpart.h
%{__perl} -pi.orig -e 's|(#include <unistd.h>)|$1\n#include <errno.h>|g' src/l64seek.h

%build
%{__make} %{?_smp_mflags} \
	CFLAGS='%{optflags} -DVERSION=\"%{real_version}\"'

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 src/gpart %{buildroot}%{_sbindir}/gpart
%{__install} -D -m0755 man/gpart.8 %{buildroot}%{_mandir}/man8/gpart.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING README
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Wed Sep 17 2003 Dag Wieers <dag@wieers.com> - 0.1-0.h
- Used contributed package. (Bert de Bruijn)

* Tue Sep 16 2003 Bert de Bruijn <bert@debruijn.be>
- Built PLD package under Red Hat.
- Added errno.h patches.
