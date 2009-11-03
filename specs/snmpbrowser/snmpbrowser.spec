# $Id$
# Authority: dries
# Screenshot: http://snmpbrowser.sourceforge.net/screenshot.png


%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

Summary: SNMP browser
Name: snmpbrowser
Version: 0.4
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://snmpbrowser.sourceforge.net/

Source: http://dl.sf.net/snmpbrowser/snmpbrowser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++
BuildRequires: gettext, zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel, fam-devel
BuildRequires: net-snmp-devel, openssl-devel
%{!?_without_selinux:BuildRequires: libselinux-devel}

%description
Snmpbrowser displays data from SNMP devices.

%prep
%setup

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib} -lssl"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/*
%{_datadir}/applnk/Applications/snmpbrowser.desktop
%{_datadir}/apps/snmpbrowser
%{_datadir}/doc/HTML/en/snmpbrowser
%{_datadir}/icons/*/*/apps/snmpbrowser.png

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sun May 30 2004 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
