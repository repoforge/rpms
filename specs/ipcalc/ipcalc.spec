# $Id$

# Authority: dag

# Upstream: Krischan Jodies <krischan@jodies.cx>

Summary: An IP subnet calculator.
Name: ipcalc
Version: 0.35
Release: 1
Group: Applications/System
License: GPL
URL: http://jodies.de/ipcalc/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://jodies.de/ipcalc-archive/%{name}-%{version}.tar.gz
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
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 ipcalc %{buildroot}%{_bindir}
%{__ln_s} -f ipcalc %{buildroot}%{_bindir}/ipcalc.pl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*

%changelog
* Thu Apr 24 2003 Dag Wieers <dag@wieers.com> - 0.35-0
- Initial package. (using DAR)
