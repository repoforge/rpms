# $Id$
# Authority: dag
# Upstream: <udpcast@udpcast.linux.lu>

%define real_version 20040222

Summary: UDP broadcast installation
Name: udpcast
Version: 0.0.20040222
Release: 1
License: GPL or BSD
Group: Applications/System
URL: http://udpcast.linux.lu/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://udpcast.linux.lu/current/udpcast-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Requires: netcfg

%description
Allows easy installation of client machines via UDP broadcast

%prep
%setup -n %{name}

%build
#%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} udp-receiver udp-sender

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 udp-sender udp-receiver %{buildroot}%{_bindir}
#%{__install} -m0644 udp-sender.1 udp-receiver.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog.txt cmd.html COPYING README*
#%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.0.20040222-1
- Updated to release 20040222.

* Thu Oct 02 2003 Dag Wieers <dag@wieers.com> - 0.0.20030831-0
- Initial package. (using DAR)
