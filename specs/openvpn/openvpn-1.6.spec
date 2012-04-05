# $Id$
# Authority: dag
# Upstream: James Yonan <jim$yonan,net>


### FIXME: Add sysv script based on own template.

Summary: Secure tunneling daemon
Name: openvpn
Version: 1.6.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://openvpn.sourceforge.net/

Source: http://dl.sf.net/openvpn/openvpn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lzo-devel, openssl-devel

%description
OpenVPN is a robust and highly flexible tunneling application that
uses all of the encryption, authentication, and certification features
of the OpenSSL library to securely tunnel IP networks over a single
UDP or TCP port. It can use the Marcus Franz Xaver Johannes Oberhumer's
LZO library for compression.

%prep
%setup

%build
%configure \
	--enable-pthread \
	--enable-iproute2
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 openvpn.8 %{buildroot}%{_mandir}/man8/openvpn.8
%{__install} -Dp -m0755 openvpn %{buildroot}%{_sbindir}/openvpn
%{__install} -Dp -m0755 sample-scripts/openvpn.init %{buildroot}%{_initrddir}/openvpn

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/openvpn/

%{__install} -d -m0755 %{buildroot}/dev/net/
%{?rh7:touch %{buildroot}/dev/net/tun}
%{?rh62:touch %{buildroot}/dev/net/tun}

%pre
if [ ! -e /dev/net/tun ]; then
        if [ ! -d /dev/net/ ]; then
                %{__install} -d -m0755 /dev/net
        fi
        mknod -m0600 /dev/net/tun c 10 200
fi


%post
/sbin/chkconfig --add openvpn

%preun
if [ $1 -eq 0 ]; then
        /sbin/service openvpn stop &>/dev/null || :
        /sbin/chkconfig --del openvpn
fi

%postun
/sbin/service openvpn condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYRIGHT.GPL INSTALL NEWS PORTS README
%doc contrib/ easy-rsa/ sample-config-files/ sample-keys/ sample-scripts/
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/openvpn/
%config %{_initrddir}/*
%{_sbindir}/openvpn
%{?rh7:%ghost /dev/net/tun}
%{?rh6:%ghost /dev/net/tun}

%changelog
* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Updated to release 1.6.0.

* Tue Nov 25 2003 Dag Wieers <dag@wieers.com> - 1.5.0-0
- Updated to release 1.5.0.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 1.5-0.beta7
- Create /dev/net/tun only for RH62 and RH73. (Rudolf Kastl)
- Updated to release 1.5-beta7.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 1.4.3-0
- Initial package. (using DAR)
