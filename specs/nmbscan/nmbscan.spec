# $Id$
# Authority: dag
# Upstream: Grégoire Barbier <gb$gbarbier,org>

Summary: NMB/SMB network scanner
Name: nmbscan
Version: 1.2.4
Release: 1
License: GPL
Group: Applications/System 
URL: http://gbarbier.free.fr/prj/dev/#nmbscan

Source: http://gbarbier.free.fr/prj/dev/down.php3?file=nmbscan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Requires: samba-client, iputils

%description
Scans a SMB shares network, using NMB and SMB protocols. Useful to acquire
information on local aera network (security audit, etc.)

Matches informations such as NMB/SMB/Windows hostname, IP address, IP
hostname, ethernet MAC address, Windows username, NMB/SMB/Windows domain name
and master browser.

Can discover all NMB/SMB/Windows hosts on a local aera network thanks to hosts
lists maintained by master browsers.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 nmbscan %{buildroot}%{_bindir}/nmbscan

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/nmbscan

%changelog
* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 1.2.4-1
- Updated to release 1.2.4.

* Sun Jun 20 2004 Dag Wieers <dag@wieers.com> - 1.2.3-1
- Updated to release 1.2.3.

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Initial package. (using DAR)
