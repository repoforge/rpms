# $Id$
# Authority: dag

%define _sbindir /sbin

Summary: IPSec VPN client compatible with Cisco equipment
Name: vpnc
Version: 0.3.2
Release: 2
License: GPL
Group: Applications/Internet
URL: http://www.unix-ag.uni-kl.de/~massar/vpnc/

Source: http://www.unix-ag.uni-kl.de/~massar/vpnc/vpnc-%{version}.tar.gz
Patch0: vpnc-0.3.2-pie.patch
Patch1: vpnc-0.3.2-64bit.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: libgcrypt-devel > 1.1.90
BuildRequires: libgcrypt-devel
Requires: kernel >= 2.4

%description
A VPN client compatible with Cisco's EasyVPN equipment.

Supports IPSec (ESP) with Mode Configuration and Xauth.  Supports only
shared-secret IPSec authentication, 3DES, MD5, and IP tunneling.

%prep
%setup
%patch0 -p1
%patch1 -p1

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
%{__install} -Dp -m0600 vpnc.conf %{buildroot}%{_sysconfdir}/vpnc.conf
%{__install} -Dp -m0644 vpnc.8 %{buildroot}%{_mandir}/man8/vpnc.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO vpnc-*
%doc %{_mandir}/man8/vpnc.8*
%config(noreplace) %{_sysconfdir}/vpnc.conf
%{_sbindir}/vpnc
%dev(c, 10, 200) /dev/tun

%changelog
* Mon Mar 07 2005 Dag Wieers <dag@wieers.com> - 0.3.2-2
- Added x86_64 fixes.

* Tue Dec 21 2004 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Updated to release 0.3.2.

* Sun Oct 10 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
