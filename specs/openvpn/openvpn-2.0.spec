# $Id$
# Authority: dag
# Upstream: James Yonan <jim$yonan,net>

%{?dist: %{expand: %%define %dist 1}}

%define prever beta11

### FIXME: Add sysv script based on own template.

Summary: Secure tunneling daemon
Name: openvpn
Version: 2.0
Release: %{?prever:0.%{prever}.}1
License: GPL
Group: Applications/Internet
URL: http://openvpn.sourceforge.net/
Source: http://dl.sf.net/openvpn/openvpn-%{version}%{?prever:_%{prever}}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: lzo-devel, openssl-devel, pkgconfig

%description
OpenVPN is a robust and highly flexible tunneling application that
uses all of the encryption, authentication, and certification features
of the OpenSSL library to securely tunnel IP networks over a single
UDP or TCP port. It can use the Marcus Franz Xaver Johannes Oberhumer's
LZO library for compression.


%prep
%setup -n %{name}-%{version}%{?prever:_%{prever}}


%build
if pkg-config openssl; then
    CFLAGS="%{optflags} `pkg-config --cflags openssl`"
    LDFLAGS="$LDFLAGS `pkg-config --libs-only-L openssl`"
fi
%configure --enable-pthread
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
# Install provided init script
%{__install} -Dp -m 0755 sample-scripts/openvpn.init \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/openvpn
# Install empty configuration directory
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/openvpn/


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/chkconfig --add openvpn

%preun
if [ $1 -eq 0 ]; then
    /sbin/service openvpn stop &>/dev/null || :
    /sbin/chkconfig --del openvpn
fi

%postun
/sbin/service openvpn condrestart &>/dev/null || :


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYRIGHT.GPL INSTALL NEWS PORTS README
%doc contrib/ easy-rsa/ sample-config-files/ sample-keys/ sample-scripts/
%dir %{_sysconfdir}/openvpn/
%config %{_sysconfdir}/rc.d/init.d/openvpn
%{_sbindir}/*
%{_mandir}/man?/*
%{?rh7:%attr(0755, root, root) %dir /dev/net}
%{?rh7:%attr(0600, root, root) %dev(c, 10, 200) /dev/net/tun}
%{?rh6:%attr(0755, root, root) %dir /dev/net}
%{?rh6:%attr(0600, root, root) %dev(c, 10, 200) /dev/net/tun}


%changelog
* Wed Oct  6 2004 Matthias Saou <http://freshrpms.net/> 2.0-0.beta11.1
- Update to 2.0_beta11.
- Add cleaner dev entries to %file instead of using mknod in post.
- Add openssl krb5 inclue error workaround for older releases.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Updated to release 1.6.0.

* Tue Nov 25 2003 Dag Wieers <dag@wieers.com> - 1.5.0-0
- Updated to release 1.5.0.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 1.5-0.beta7
- Create /dev/net/tun only for RH62 and RH73. (Rudolf Kastl)
- Updated to release 1.5-beta7.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 1.4.3-0
- Initial package. (using DAR)
