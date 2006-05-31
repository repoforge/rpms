# $Id$
# Authority: dag
# Upstream: <udpcast$udpcast,linux,lu>

Summary: UDP broadcast installation
Name: udpcast
%define real_version 20060525
Version: 0.0.20060525
Release: 1
License: GPL or BSD
Group: Applications/System
URL: http://udpcast.linux.lu/

Source: http://udpcast.linux.lu/download/udpcast-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Requires: netcfg

%description
Allows easy installation of client machines via UDP broadcast

%prep
%setup -n %{name}-%{real_version}

%build
#%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} udp-receiver udp-sender

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 udp-receiver %{buildroot}%{_bindir}/udp-receiver
%{__install} -Dp -m0755 udp-sender %{buildroot}%{_bindir}/udp-sender
#%{__install} -Dp -m0644 udp-receiver.1 %{buildroot}%{_mandir}/man1/udp-receiver.1
#%{__install} -Dp -m0644 udp-sender.1 %{buildroot}%{_mandir}/man1/udp-sender.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog.txt cmd.html COPYING
#%doc Changelog.txt cmd.html COPYING README*
#%doc %{_mandir}/man1/udp-receiver.1*
#%doc %{_mandir}/man1/udp-sender.1*
%{_bindir}/udp-receiver
%{_bindir}/udp-sender

%changelog
* Wed May 31 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.20060525-1
- Updated to release 20060525.

* Tue Mar 28 2006 Dag Wieers <dag@wieers.com> - 0.0.20060325-1
- Updated to release 20060325.

* Tue Mar 08 2005 Dag Wieers <dag@wieers.com> - 0.0.20050307-1
- Updated to release 20050307.

* Sun Feb 27 2005 Dag Wieers <dag@wieers.com> - 0.0.20050226-1
- Updated to release 20050226.

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.0.20040222-1
- Updated to release 20040222.

* Thu Oct 02 2003 Dag Wieers <dag@wieers.com> - 0.0.20030831-0
- Initial package. (using DAR)
