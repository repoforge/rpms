# $Id$
# Authority: dag
# Upstream: Krischan Jodies <krischan$jodies,cx>

Summary: IP subnet calculator
Name: ipcalc
Version: 0.41
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://jodies.de/ipcalc/

Source: http://jodies.de/ipcalc-archive/ipcalc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ipcalc takes an IP address and netmask and calculates the resulting
broadcast, network, Cisco wildcard mask, and host range. By giving
a second netmask, you can design subnets and supernets. It is also
intended to be a teaching tool and presents the subnetting results
as easy-to-understand binary values.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 ipcalc %{buildroot}%{_bindir}/ipcalc
%{__ln_s} -f ipcalc %{buildroot}%{_bindir}/ipcalc.pl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Updated to release 0.41.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.37-1.2
- Rebuild for Fedora Core 5.

* Fri May 14 2003 Dag Wieers <dag@wieers.com> - 0.37-1
- updated to release 0.37.

* Thu Apr 24 2003 Dag Wieers <dag@wieers.com> - 0.35-0
- Initial package. (using DAR)
