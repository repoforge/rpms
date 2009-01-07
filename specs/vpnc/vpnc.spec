# $Id$
# Authority: dag

%define _sbindir /sbin

Summary: IPSec VPN client compatible with Cisco equipment
Name: vpnc
Version: 0.5.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.unix-ag.uni-kl.de/~massar/vpnc/

Source: http://www.unix-ag.uni-kl.de/~massar/vpnc/vpnc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgcrypt-devel
Requires: kernel >= 2.4

%description
A VPN client compatible with Cisco's EasyVPN equipment.

Supports IPSec (ESP) with Mode Configuration and Xauth.  Supports only
shared-secret IPSec authentication, 3DES, MD5, and IP tunneling.

%prep
%setup

%{__cat} <<EOF >vpnc.conf
### This is the gateway configuration
#IPSec gateway my.vpn.gateway
#IPSec ID my.ipsec.id
#IPSec secret mysecret

### Put your username here
#Xauth username
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 vpnc %{buildroot}%{_sbindir}/vpnc
%{__install} -Dp -m0755 vpnc-disconnect %{buildroot}%{_sbindir}/vpnc-disconnect
%{__install} -Dp -m0755 pcf2vpnc %{buildroot}%{_sbindir}/pcf2vpnc
%{__install} -Dp -m0600 vpnc.conf %{buildroot}%{_sysconfdir}/vpnc/vpnc.conf
%{__install} -Dp -m0600 vpnc-script %{buildroot}%{_sysconfdir}/vpnc/vpnc-script
%{__install} -Dp -m0644 vpnc.8 %{buildroot}%{_mandir}/man8/vpnc.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%doc %{_mandir}/man8/vpnc.8*
%dir %{_sysconfdir}/vpnc
%config(noreplace) %{_sysconfdir}/vpnc/vpnc.conf
%config(noreplace) %{_sysconfdir}/vpnc/vpnc-script
%{_sbindir}/vpnc
%{_sbindir}/vpnc-disconnect
%{_sbindir}/pcf2vpnc
%dev(c, 10, 200) /dev/tun

%changelog
* Tue Jan 06 2009 Kenneth Porter <shiva+vpncrpm@sewingwitch.com> - 0.5.3-1
- Update to 0.5.3.
- Include helper scripts.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.3-1.2
- Rebuild for Fedora Core 5.

* Fri Jun 24 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.3-1
- Update to release 0.3.3.

* Mon Mar 07 2005 Dag Wieers <dag@wieers.com> - 0.3.2-2
- Added x86_64 fixes.

* Tue Dec 21 2004 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Updated to release 0.3.2.

* Sun Oct 10 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
