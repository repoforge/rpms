# $Id$
# Authority: yury
# Upstream: Con Kolivas <kernel$kolivas,org>

%define curl_version 7.19.7

%{?el5:%define _with_static_curl 1}

Summary: CPU/GPU Miner by Con Kolivas
Name: cgminer
Version: 1.4.1
Release: 1%{?dist}
License: GPLv2
Group: Applications/Internet
URL: http://forum.bitcoin.org/index.php?topic=28402.0

Source0: http://ck.kolivas.org/apps/%{name}/%{name}-%{version}.tar.bz2
%{?_with_static_curl:Source1: http://curl.haxx.se/download/curl-%{curl_version}.tar.bz2}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc
BuildRequires: make
BuildRequires: yasm >= 1.1.0

%if 0%{?el6}
BuildRequires: libcurl-devel
%endif

BuildRequires: ncurses-devel
BuildRequires: pkgconfig >= 0.9.0

%if 0%{?_with_static_curl}
### Curl BuildRequires
BuildRequires: krb5-devel
BuildRequires: libidn-devel
BuildRequires: nss-devel
BuildRequires: openldap-devel
BuildRequires: openssh-clients
BuildRequires: openssh-server
BuildRequires: pkgconfig
BuildRequires: valgrind
BuildRequires: zlib-devel
%endif

%description
This is a multi-threaded CPU and GPU miner for Bitcoin.

The present package is compiled without support for GPU mining, so only
CPU mining is possible at this moment.

%prep
%setup
%{?_with_static_curl:%setup -T -D -a 1}

%build

%if 0%{?_with_static_curl}
### Build curl
pushd curl-%{curl_version}
RESULT_DIR="$(pwd)/result"

./configure \
    --prefix="$RESULT_DIR" \
    --exec-prefix="$RESULT_DIR" \
    --disable-manual \
    --disable-shared \
    --enable-ipv6 \
    --enable-ldaps \
    --enable-static \
    --without-libssh2 \
    --without-ssl \
    --with-ca-bundle="%{_sysconfdir}/pki/tls/certs/ca-bundle.crt" \
    --with-gssapi="%{_prefix}/kerberos" \
    --with-libidn \
    --with-nss \

%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" install
popd

# Curl doesn't respect multilib and installs *.pc in lib vs. lib64
PKG_CONFIG_PATH="$RESULT_DIR/lib/pkgconfig:$PKG_CONFIG_PATH" ; export PKG_CONFIG_PATH

# This is for curl-config
PATH="$RESULT_DIR/bin:$PATH" ; export PATH

%endif

# Build cgminer
%configure
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -O3 -Wall"

%install
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/cgminer
%exclude %{_bindir}/*.cl

%changelog
* Sun Jul 24 2011 Yury V. Zaytsev <yury@shurup.com> - 1.4.1-1
- Static build against libcurl from RHEL6 on RHEL5.
- Updated to release 1.4.1.

* Sat Jul 23 2011 Yury V. Zaytsev <yury@shurup.com> - 1.4.0-1
- Updated to release 1.4.0.

* Wed Jul 20 2011 Yury V. Zaytsev <yury@shurup.com> - 1.3.1-1
- Updated to release 1.3.1.

* Tue Jul 19 2011 Yury V. Zaytsev <yury@shurup.com> - 1.3.0-1
- Updated to release 1.3.0.

* Mon Jul 18 2011 Yury V. Zaytsev <yury@shurup.com> - 1.2.8-1
- Updated to release 1.2.8.

* Sun Jul 17 2011 Yury V. Zaytsev <yury@shurup.com> - 1.2.7-1
- Initial package.
