# $Id$
# Authority: yury
# Upstream: Jari "Rakshasa" Sundell <sundell,software$gmail,com>

%define curl_version 7.19.6

Summary: Console-based BitTorrent client
Name: rtorrent
Version: 0.8.6
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://libtorrent.rakshasa.no/

Source0: http://libtorrent.rakshasa.no/downloads/rtorrent-%{version}.tar.gz
Source1: http://curl.haxx.se/download/curl-%{curl_version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: libsigc++20-devel
BuildRequires: libtorrent-devel >= 0.12.5
BuildRequires: ncurses-devel

### Curl BuildRequires from Rawhide (no stunnel!)
BuildRequires: krb5-devel
BuildRequires: libidn-devel
BuildRequires: nss-devel
BuildRequires: openldap-devel
BuildRequires: openssh-clients
BuildRequires: openssh-server
BuildRequires: pkgconfig
BuildRequires: valgrind
BuildRequires: zlib-devel

%description
rTorrent is a console-based BitTorrent client. It aims to be a
fully-featured and efficient client with the ability to run in the 
background using screen. It supports fast-resume and session
management.

%prep
%setup
%setup -T -D -a 1

%build

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
    --with-nss
#    --libdir="$RESULT_DIR/usr/%{_lib}" \

%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" install
popd

# Build rtorrent
PKG_CONFIG_PATH="$RESULT_DIR/usr/%{_lib}/pkgconfig:$PKG_CONFIG_PATH" ; export PKG_CONFIG_PATH

%configure
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/rtorrent.1*
%{_bindir}/rtorrent

%changelog
* Mon Dec 28 2009 Yury V. Zaytsev <yury@shurup.com> - 0.8.6-2
- Removed stunnel build requirement that somehow got in from rawhide
  (and is not really needed), that was causing build failures as
  stunnel for RHEL is only available from EPEL. Sorry!

* Tue Dec 15 2009 Yury V. Zaytsev <yury@shurup.com> - 0.8.6-1
- Updated to release 0.8.6.

* Wed Nov 11 2009 Yury V. Zaytsev <yury@shurup.com> - 0.8.5-3
- Minor refinements by Steve Huff (thanks)!

* Tue Nov 3 2009 Yury V. Zaytsev <yury@shurup.com> - 0.8.5-2
- Static build against latest curl.

* Tue Oct 27 2009 Steve Huff <shuff@vecna.org> - 0.8.5-1
- Updated to release 0.8.5.

* Sun Jul 19 2009 Dag Wieers <dag@wieers.com> - 0.8.4-2
- Rebuild against libtorrent.

* Thu Jan  1 2009 Dries Verachtert <dries@ulyssis.org> - 0.8.4-1
- Updated to release 0.8.4.

* Tue Jan 29 2008 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1
- Updated to release 0.8.0.

* Mon Dec 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.9-1
- Updated to release 0.7.9.

* Fri Aug 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.6-1
- Updated to release 0.7.6.

* Wed Apr 25 2007 Dag Wieers <dag@wieers.com> - 0.7.4-1
- Updated to release 0.7.4.

* Mon Jan 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Updated to release 0.7.1.

* Fri Dec 15 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Updated to release 0.7.0.

* Mon Nov 13 2006 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Updated to release 0.6.4.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.3-1
- Updated to release 0.6.3.

* Mon Apr 10 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.3-1
- Updated to release 0.5.3.

* Mon Apr 10 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Thu Mar 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.5-1
- Updated to release 0.4.5.

* Thu Jan 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.2-1
- Initial package.
