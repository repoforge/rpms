# $Id$
# Authority: dag
# Upstream: <open1x-xsupplicant$lists,sourceforge,net>


%{?el4:%define _without_wireless_tools_devel 1}
%{?el3:%define _without_wireless_tools_devel 1}
%{?rh9:%define _without_wireless_tools_devel 1}
%{?rh7:%define _without_wireless_tools_devel 1}
%{?el2:%define _without_wireless_tools_devel 1}

Summary: Open source implement of IEEE 802.1x
Name: xsupplicant
Version: 1.2.8
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://open1x.sourceforge.net/

Source: http://dl.sf.net/open1x/xsupplicant-%{version}.tar.gz
Patch0: xsupplicant-1.2.2-docsfix.patch
Patch2: xsupplicant-1.2.8-nocompilerh-systemheaders.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel >= 0.9.7, byacc, flex, wireless-tools
%{!?_without_wireless_tools_devel:BuildRequires: wireless-tools-devel}
Requires: /sbin/ldconfig, openssl >= 0.9.7

%description
xsupplicant allows a GNU/Linux or BSD workstation to authenticate with
a RADIUS server using 802.1x and various EAP protocols. The intended
use is for computers with wireless LAN connections to complete a strong
authentication before joining the network.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1
%patch2 -p1

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure*

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0600 etc/xsupplicant.conf %{buildroot}%{_sysconfdir}/xsupplicant.conf

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING INSTALL LICENSE README TODO doc/README* doc/standards/ doc/*.html etc/*.conf
%config(noreplace) %{_sysconfdir}/xsupplicant.conf
%{_bindir}/config-parser
%{_bindir}/xsup_get_state
%{_bindir}/xsup_monitor
%{_bindir}/xsup_ntpwdhash
%{_bindir}/xsup_set_pwd
%{_sbindir}/xsupplicant

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/xsupconfcheck.h
%{_includedir}/xsupconfig.h
%{_includedir}/xsupconfwrite.h
%{_includedir}/xsupgui.h
%{_libdir}/libxsup*.a

%changelog
* Mon May 14 2007 Dag Wieers <dag@wieers.com> - 1.2.8-1
- Updated to release 1.2.8.

* Sun Feb 13 2005 Dag Wieers <dag@wieers.com> - 1.0.1-2
- Added default xsupplicant.conf.

* Tue Jan 11 2005 Chris Weyl <cweyl@alumni.drew.edu> - 1.0.1-1
- Initial RPM release.
