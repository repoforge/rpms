# $Id$
# Authority: dag
# Upstream: Tangui Morlier <tmorlier$lri,fr>

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

Summary: User level sandbox designed for grid technologies
Name: s4g
Version: 0.8.1
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.lri.fr/~tmorlier/S4G/

Source: http://www.lri.fr/~tmorlier/S4G/s4g-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
S4G is an open source user level sandbox designed for grid technologies.
It offers a secure execution environment for untrusted applications.
Efficient and lightweight, it does not require to modify your linux kernel,
to insert a specific module nor to have special administrator rights.

%prep
%setup

%build
%{__perl} -pi -e 's|#include <linux/user.h>|#include <sys/user.h>|g;' common.h
%{__make} %{?_smp_mflags} \
	FLAGS="-Wall %{optflags} -I%{_includedir}"
#	FLAGS="%{optflags} -I%{_includedir} -I/%{_lib}/modules/%{kernel}/build/include"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 sandbox %{buildroot}%{_bindir}/sandbox

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%{_bindir}/sandbox

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1.2
- Rebuild for Fedora Core 5.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Initial package. (using DAR)
