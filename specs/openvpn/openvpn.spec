# $Id$
# Authority: dag
# Upstream: James Yonan <jim$yonan,net>

### PKCS#11 support (optional)
%define _with_pkcs11 1

Summary: Robust and highly flexible VPN daemon
Name: openvpn
Version: 2.3.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://openvpn.net/

Source: http://swupdate.openvpn.net/community/releases/%{name}-%{version}.tar.gz
Patch:  openvpn-2.3.1-initscript.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lzo-devel >= 2.03
BuildRequires: openssl-devel >= 0.9.6
BuildRequires: pkgconfig
BuildRequires: pam-devel
%if 0%{?_with_pkcs11}
BuildRequires: pkcs11-helper-devel
Requires: pkcs11-helper
%endif
Requires: lzo
Requires: openssl
Requires: /sbin/chkconfig
Requires: /sbin/service
# For /sbin/ip
BuildRequires: iproute
# For /sbin/ip
Requires: iproute

%description
OpenVPN is a robust and highly flexible tunneling application.

OpenVPN supports SSL/TLS security, ethernet bridging, TCP or UDP tunnel
transport through proxies or NAT, support for dynamic IP addresses and
DHCP, scalability to hundreds or thousands of users, and portability to
most major OS platforms.

%prep
%setup

### Fix provided initscript
%patch -p0

### Fix provided man-file
%{__sed} -i -e 's,%{_datadir}/openvpn/plugin,%{_libdir}/openvpn/plugin,' doc/openvpn.8

%build
if pkg-config openssl; then
    export CFLAGS="%{optflags} $(pkg-config --cflags openssl)"
    export LDFLAGS="$LDFLAGS $(pkg-config --libs-only-L openssl)"
fi
%configure \
    --program-prefix="%{?_program_prefix}" \
    --enable-iproute2 \
    %if 0%{?_with_pkcs11}
    --enable-pkcs11 \
    %else
    --disable-pkcs11 \
    %endif
    --enable-password-save \
    --enable-plugins \
    --enable-plugin-down-root \
    --enable-plugin-auth-pam
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
find %{buildroot} -name '*.la' | xargs rm -f

### Install provided init script
%{__install} -Dp -m0755 distro/rpm/openvpn.init.d.rhel %{buildroot}%{_initrddir}/openvpn

### Install empty configuration directory
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/openvpn/

### Disable find-requires for documentation
find contrib/ sample/ -type f -exec %{__chmod} -x {} \;

%clean
%{__rm} -rf %{buildroot}

%pre
getent group openvpn &>/dev/null || groupadd -r openvpn
getent passwd openvpn &>/dev/null || \
    /usr/sbin/useradd -r -g openvpn -s /sbin/nologin \
    -c OpenVPN -d /etc/openvpn openvpn

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add openvpn
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service openvpn stop &>/dev/null || :
    /sbin/chkconfig --del openvpn
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service openvpn condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYRIGHT.GPL INSTALL NEWS PORTS README
%doc contrib src/plugins/*/README.* doc/README.plugins sample
%doc %{_mandir}/man8/openvpn.8*
%config %dir %{_sysconfdir}/openvpn/
%config %{_initrddir}/openvpn
%{_includedir}/openvpn-plugin.h
%{_libdir}/openvpn/
%{_sbindir}/openvpn
%exclude %{_datadir}/doc/openvpn

%changelog
* Sat Jun 08 2013 Denis Fateyev <denis@fateyev.com> - 2.3.2-1
- Updated to version 2.3.2

* Fri Mar 16 2012 Denis Fateyev <denis@fateyev.com> - 2.2.2-1
- Updated to version 2.2.2

* Sun Jun 05 2011 Yury V. Zaytsev <yury@shurup.com> - 2.2.0-3
- Fixed typo in the initscript patch, see gh-11 (thanks, Martin!)

* Mon May 23 2011 Steve Huff <shuff@vecna.org> - 2.2.0-2
- Updated to version 2.2.0.

* Fri Feb 18 2011 Denis Fateyev <denis@fateyev.com> - 2.1.4-2
- Some spec cleanup, added some patches from Fedora

* Tue Nov 30 2010 Christoph Maser <cmaser@gmx.de> - 2.1.4-1
- Updated to version 2.1.4.

* Fri Feb 02 2007 Dag Wieers <dag@wieers.com> - 2.0.9-1
- Updated to release 2.0.9.

* Sat Apr 29 2006 Dag Wieers <dag@wieers.com> - 2.0.7-1
- Updated to release 2.0.7.

* Thu Mar 23 2006 Dag Wieers <dag@wieers.com> - 2.0.5-1
- Updated to release 2.0.5.

* Thu Sep 08 2005 Dag Wieers <dag@wieers.com> - 2.0.2-1
- Updated to release 2.0.2.

* Thu Aug 18 2005 Dag Wieers <dag@wieers.com> - 2.0.1-1
- Added pam-devel build requirement. (Greg Cope)
- Updated to release 2.0.1.

* Sat Apr 30 2005 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Mon Apr 04 2005 Dag Wieers <dag@wieers.com> - 2.0-0.rc20.1
- Updated to release 2.0_rc20.

* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 2.0-0.rc19.2
- Disabled find-requires for %%doc.

* Fri Apr 01 2005 Dag Wieers <dag@wieers.com> - 2.0-0.rc19.1
- Updated to release 2.0_rc19.

* Wed Oct  6 2004 Matthias Saou <http://freshrpms.net/> 2.0-0.beta11.1
- Update to 2.0_beta11.
- Add cleaner dev entries to "file" instead of using mknod in post.
- Add openssl krb5 include error workaround for older releases.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Updated to release 1.6.0.

* Tue Nov 25 2003 Dag Wieers <dag@wieers.com> - 1.5.0-0
- Updated to release 1.5.0.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 1.5-0.beta7
- Create /dev/net/tun only for RH62 and RH73. (Rudolf Kastl)
- Updated to release 1.5-beta7.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 1.4.3-0
- Initial package. (using DAR)
