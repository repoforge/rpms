# $Id$
# Authority: dag
# Upstream: <oorexx-devel$lists,sourceforge,net>

%define real_name ooRexx

Summary: Open Object Rexx
Name: oorexx
Version: 3.1.1
Release: 1%{?dist}
License: CPL
Group: Development/Languages
URL: http://www.oorexx.org/

Source: http://dl.sf.net/oorexx/ooRexx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, ncurses-devel

ExclusiveArch: i386
Obsoletes: ooRexx <= %{version}-%{release}
Obsoletes: oorexx-libs <= %{version}-%{release}

%description
Open Object Rexx is an object-oriented scripting language. The language
is designed for "non-programmer" type users, so it is easy to learn
and easy to use, and provides an excellent vehicle to enter the world
of object-oriented programming without much effort.

It extends the procedural way of programming with object-oriented
features that allow you to gradually change your programming style
as you learn more about objects.

%prep
%setup -n %{real_name}-%{version}

### Fix shell interpreter path
%{__perl} -pi.orig -e 's|^#!/usr/bin/sh|#!/bin/sh|g' samples/unix/trexx

%build
%configure \
	--disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up docdir
%{__find} samples/ -name 'Makefile*' | xargs %{__rm} -f

%{__rm} -f %{buildroot}%{_datadir}/ooRexx/rexx.{csh,sh}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc CPLv1.0.txt INSTALL samples/
%doc %{_mandir}/man1/rexx*.1*
%doc %{_mandir}/man1/rx*.1*
%{_bindir}/oorexx-config
%{_bindir}/rexx*
%{_bindir}/rx*
%{_datadir}/ooRexx/
%{_includedir}/rexx.h
%{_libdir}/ooRexx/

%changelog
* Mon Jan 15 2007 Dag Wieers <dag@wieers.com> - 3.1.1-1
- Updated to release 3.1.1.

* Mon Mar 28 2005 Dag Wieers <dag@wieers.com> - 3.0.0-1
- Initial package. (using DAR)
