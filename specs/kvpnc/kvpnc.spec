# $Id$
# Authority: dries

Summary: Frontend for various VPN clients
Name: kvpnc
Version: 0.8.8
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://home.gna.org/kvpnc/

Source: http://download.gna.org/kvpnc/kvpnc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, kdelibs-devel >= 3.4

%description
KVpnc is a KDE frontend for various VPN clients. It supports Cisco VPN (vpnc) 
and IPSec (FreeS/WAN, racoon). vpnc is a replacement for the Cisco VPN client, 
and is used as client for the cisco3000 VPN Concentrator. FreeS/WAN 
(OpenS/WAN) is a IPSec client for Linux 2.4.x, and raccoon is a IPSec client 
for Linux 2.6.x and *BSD. It also supports PPTP (pptpclient) and OpenVPN.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/kvpnc
%{_datadir}/applnk/kvpnc.desktop
%{_datadir}/apps/kvpnc/
%{_datadir}/doc/HTML/*/kvpnc/
%{_datadir}/doc/HTML/kvpnc/
%{_datadir}/icons/*/*/apps/kvpnc.*

%changelog
* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.8-1
- Updated to release 0.8.8.

* Sun Dec 15 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.7-1
- Updated to release 0.8.7.

* Mon Oct 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.6.1-1
- Updated to release 0.8.6.1.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.5.1-1
- Updated to release 0.8.5.1.

* Sat Apr 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.4-1
- Initial package.
