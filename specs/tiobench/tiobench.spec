# $Id$
# Authority: dag
# Upstream: Mika Kuoppala <miku$iki,fi>

Summary: Threaded IO benchmarking utility
Name: tiobench
Version: 0.3.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://sf.net/projects/tiobench/

Source: http://dl.sf.net/tiobench/tiobench-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Portable, robust, fully-threaded I/O benchmark program

%prep
%setup

### Enable large file support.
%{__perl} -pi.orig -e 's|^#(DEFINES=-DLARGEFILES)$|$1|' Makefile

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 tiobench.pl %{buildroot}%{_bindir}/tiobench
%{__install} -Dp -m0755 tiotest %{buildroot}%{_bindir}/tiotest

### Clean up docs
%{__rm} -rf scripts/CVS

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING README scripts/ TODO
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.3-1.2
- Rebuild for Fedora Core 5.

* Fri Apr 16 2004 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Initial package. (using DAR)
