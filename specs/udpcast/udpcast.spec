# $Id$
# Authority: dag
# Upstream: <udpcast$udpcast,linux,lu>

Summary: UDP broadcast file distribution and installation
Name: udpcast
%define real_version 20081116
Version: 0.0.20081116
Release: 1%{?dist}
License: GPL or BSD
Group: Applications/System
URL: http://udpcast.linux.lu/

Source: http://udpcast.linux.lu/download/udpcast-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: m4
#Requires: netcfg

%description
udpcast is an application for multicasting data to multiple targets.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
#    --prefix="%{buildroot}%{_prefix}" \
#    --mandir="%{buildroot}%{_mandir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog.txt cmd.html COPYING *.txt
%doc %{_mandir}/man1/udp-receiver.1*
%doc %{_mandir}/man1/udp-sender.1*
%{_includedir}/udpcast/
%{_sbindir}/udp-receiver
%{_sbindir}/udp-sender

%changelog
* Wed Nov 19 2008 Dag Wieers <dag@wieers.com> - 0.0.20081116-1
- Updated to release 20081116.

* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 0.0.20080914-1
- Updated to release 20080914.

* Mon Jun 04 2007 Dag Wieers <dag@wieers.com> - 0.0.20070602-1
- Updated to release 20070602.

* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 0.0.20070323-1
- Updated to release 20070323.

* Mon Mar 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.20070306-1
- Updated to release 20070306.

* Sun Feb 18 2007 Dag Wieers <dag@wieers.com> - 0.0.20070218-1
- Updated to release 20070218.

* Sun Feb 11 2007 Dag Wieers <dag@wieers.com> - 0.0.20070205-1
- Updated to release 20070205.

* Wed Jan 31 2007 Dag Wieers <dag@wieers.com> - 0.0.20070131-1
- Updated to release 20070131.

* Wed Jan 31 2007 Dag Wieers <dag@wieers.com> - 0.0.20070129-1
- Updated to release 20070129.

* Thu Dec 21 2006 Dag Wieers <dag@wieers.com> - 0.0.20060929-1
- Updated to release 20060929.

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
