# $Id$
# Authority: dag
# Upstream: <open1x-xsupplicant$lists,sourceforge,net>

Summary: Open source implement of IEEE 802.1x
Name: xsupplicant
Version: 1.0.1
Release: 1
License: GPL
Group: System Environment/Base
URL: http://www.open1x.org/

Source: http://dl.sf.net/open1x/xsupplicant-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel >= 0.9.7, byacc, flex
Requires: /sbin/ldconfig, openssl >= 0.9.7

%description
This software allows a GNU/Linux or BSD workstation to authenticate with
a RADIUS server using 802.1x and various EAP protocols.  The intended
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

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure*

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0600 etc/xsupplicant.conf %{buildroot}%{_sysconfdir}/xsupplicant.conf

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README README.wireless_cards doc/html/ doc/txt/ doc/README* etc/*.conf
%config(noreplace) %{_sysconfdir}/xsupplicant.conf
%{_bindir}/config-parser
%{_bindir}/xsup_monitor
%{_bindir}/xsup_set_pwd
%{_sbindir}/xsupplicant

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libcardif.a

%changelog
* Sun Feb 13 2005 Dag Wieers <dag@wieers.coM> - 1.0.1-2
- Added default xsupplicant.conf.

* Tue Jan 11 2005 Chris Weyl <cweyl@alumni.drew.edu> - 1.0.1-1
- Initial RPM release.
