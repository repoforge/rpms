# $Id$
# Authority: dag

Summary: IBM ThinkPad configuration tools
Name: tpctl
Version: 4.14
Release: 1
License: GPL
Group: System Environment/Base
URL: http://tpctl.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/tpctl/tpctl_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, perl
Requires: kernel-module-thinkpad >= 3.2, perl

Obsoletes: tpctl-apmiser

%description
tpctl is a package of IBM ThinkPad configuration tools for Linux.

%prep
%setup

### FIXME: Remove chown/chgrp from Makefile. (Please fix upstream)
%{__perl} -pi.orig -e 's| -o 0 -g 0 | |' Makefile

%build
%{__make} %{?_smp_mflags} all \
	CFLAGS="%{optflags}"
%{__cp} -av apmiser/README ./README.apmiser

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man1
%makeinstall \
	PATH_SBIN="%{buildroot}%{_sbindir}/" \
	PATH_BIN="%{buildroot}%{_bindir}/" \
	PATH_LIB="%{buildroot}%{_libdir}/" \
	PATH_MAN="%{buildroot}%{_mandir}/"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README* SUPPORTED* TROUBLE* VGA-MODES
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_libdir}/*.so.*
%{_bindir}/*

%changelog
* Sun Jun 20 2004 Dag Wieers <dag@wieers.com> - 4.14-1
- Updated to release 4.14.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 4.10-0
- Updated to release 4.10.

* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 4.8-0
- Updated to release 4.8.

* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 4.4-0
- Updated to release 4.4.

* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 4.3-0
- Initial package. (using DAR)
