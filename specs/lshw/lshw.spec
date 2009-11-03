# $Id$
# Authority: dag
# Upstream: Lyonel Vincent <lyonel$ezix,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define _without_gtk24 1}
%{?el3:%define _without_gtk24 1}
%{?rh9:%define _without_gtk24 1}
%{?rh8:%define _without_gtk24 1}
%{?rh7:%define _without_gtk24 1}
%{?el2:%define _without_gtk24 1}

Summary: Hardware lister
Name: lshw
%define real_version B.02.14
Version: 2.14
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.ezix.org/software/lshw.html

Source: http://www.ezix.org/software/files/lshw-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
lshw is a small tool to provide detailed informaton on the hardware
configuration of the machine. It can report exact memory configuration,
firmware version, mainboard configuration, CPU version and speed, cache
configuration, bus speed, etc. on DMI-capable x86 systems and on some
PowerPC machines (PowerMac G4 is known to work).

Information can be output in plain text, XML or HTML.

%package gui
Summary: Graphical hardware lister
Group: Applications/System
%{!?_without_gtk24:BuildRequires: gtk2-devel >= 2.4}
Requires: %{name} = %{version}-%{release}

%description gui
lshw is a small tool to provide detailed informaton on the hardware
configuration of the machine. It can report exact memory configuration,
firmware version, mainboard configuration, CPU version and speed, cache
configuration, bus speed, etc. on DMI-capable x86 systems and on some
PowerPC machines (PowerMac G4 is known to work).

Information can be output in plain text, XML or HTML.

%prep
%setup -n %{name}-%{real_version}

%{__perl} -pi.orig -e 's|-g -Wall -Os|%{optflags}|' src/Makefile

%build
%{__make} %{?_smp_mflags}
%if %{!?_without_gtk24:1}0
%{__make} %{?_smp_mflags} gui
%endif

%install
%{__rm} -rf %{buildroot}
%{__make} install \
    DESTDIR="%{buildroot}" \
    PREFIX="%{_prefix}" \
    SBINDIR="%{_sbindir}" \
    MANDIR="%{_mandir}" \
    INSTALL="%{__install} -p"

%if %{!?_without_gtk24:1}0
%{__make} install-gui\
    DESTDIR="%{buildroot}" \
    PREFIX="%{_prefix}" \
    SBINDIR="%{_sbindir}" \
    MANDIR="%{_mandir}" \
    INSTALL="%{__install} -p"
%{__ln_s} -f gtk-lshw %{buildroot}%{_sbindir}/lshw-gui
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING docs/*
%doc %{_mandir}/man1/lshw.1*
%{_sbindir}/lshw
%{_datadir}/lshw/

%if %{!?_without_gtk24:1}0
%files gui
%defattr(-, root, root, 0755)
%doc COPYING
%{_sbindir}/gtk-lshw
%{_sbindir}/lshw-gui
%endif

%changelog
* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 2.14-1
- Updated to release B.02.14.

* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 2.13-1
- Updated to release B.02.13.

* Sun Oct 14 2007 Dag Wieers <dag@wieers.com> - 2.12.1-1
- Updated to release B.02.12.01.

* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 2.12-1
- Updated to release B.02.12.

* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 2.11.1-1
- Updated to release B.02.11.01.

* Thu Jul 26 2007 Dag Wieers <dag@wieers.com> - 2.11-1
- Updated to release B.02.11.

* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 2.10-1
- Updated to release B.02.10.

* Wed Nov 08 2006 Dag Wieers <dag@wieers.com> - 2.09-1
- Updated to release B.02.09.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 2.08.01-1
- Updated to release B.02.08.01.

* Thu May 11 2006 Dag Wieers <dag@wieers.com> - 2.08-1
- Updated to release B.02.08.

* Sun Mar 05 2006 Dag Wieers <dag@wieers.com> - 2.07-1
- Updated to release B.02.07.

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 2.06-1
- Updated to release B.02.06.

* Thu Jul 21 2005 Dag Wieers <dag@wieers.com> - 2.05.01-1
- Updated to release B.02.05.01.

* Wed Jul 20 2005 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release B.02.05.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 2.04-1
- Updated to release B.02.04.

* Mon Feb 07 2005 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release B.02.03.

* Fri Jan 21 2005 Dag Wieers <dag@wieers.com> - 2.02-1
- Updated to release B.02.02.

* Tue Dec 21 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)
