# $Id: $

# Authority: dries
# Upstream: 

Summary: SNMP browser
Name: snmpbrowser
Version: 0.4
Release: 1
License: GPL
Group: Applications/Internet
URL: http://snmpbrowser.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/snmpbrowser/snmpbrowser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++
BuildRequires: gettext, XFree86-devel, zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel
BuildRequires: net-snmp-devel, openssl-devel
%{?fc2:BuildRequires: libselinux-devel}

# Screenshot: http://snmpbrowser.sourceforge.net/screenshot.png

%description
Snmpbrowser displays data from SNMP devices.

%prep
%setup

%build
%configure LDFLAGS=-lssl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
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
%{_datadir}/apps/snmpbrowser/icons/*/*/actions/*_node.png
%{_datadir}/apps/snmpbrowser/snmpbrowserui.rc
%{_datadir}/doc/HTML/en/snmpbrowser
%{_datadir}/icons/*/*/apps/snmpbrowser.png

%changelog
* Sun May 30 2004 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
