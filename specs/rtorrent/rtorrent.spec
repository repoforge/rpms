# $Id$
# Authority: yury
# Upstream: Jari "Rakshasa" Sundell <sundell,software$gmail,com>

### More unification with curl version (7.19.7 shipped with el6)
%{?el5:%define curl_version 7.19.7}

Summary: Console-based BitTorrent client
Name: rtorrent
Version: 0.8.9
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://libtorrent.rakshasa.no/

Source0: http://libtorrent.rakshasa.no/downloads/rtorrent-%{version}.tar.gz
%{?curl_version:Source1: http://curl.haxx.se/download/curl-%{curl_version}.tar.bz2}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: libsigc++20-devel
BuildRequires: libtorrent-devel >= 0.12.9
BuildRequires: ncurses-devel

BuildRequires: krb5-devel
BuildRequires: libidn-devel
BuildRequires: openldap-devel
BuildRequires: openssh-clients
BuildRequires: openssh-server
BuildRequires: pkgconfig
BuildRequires: valgrind
BuildRequires: zlib-devel

%{?el6:BuildRequires: curl-devel}
%{?el6:BuildRequires: cppunit}
%{?el6:BuildRequires: cppunit-devel}
BuildRequires: xmlrpc-c-devel


%description
rTorrent is a console-based BitTorrent client. It aims to be a
fully-featured and efficient client with the ability to run in the 
background using screen. It supports fast-resume and session
management.

%prep
%setup
%{?curl_version:%setup -T -D -a 1}

%build
%if %{?curl_version:1}0
### Build curl
pushd curl-%{curl_version}
RESULT_DIR="$(pwd)/result"

./configure \
    --prefix="$RESULT_DIR" \
    --exec-prefix="$RESULT_DIR" \
    --disable-manual \
    --disable-shared \
    --enable-ipv6 \
    --enable-static \
    --without-libssh2 \
    --without-ssl \
    --with-ca-bundle="%{_sysconfdir}/pki/tls/certs/ca-bundle.crt" \
    --with-gssapi="%{_prefix}/kerberos" \
    --with-libidn

%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" install
popd

### Build rtorrent
PKG_CONFIG_PATH="$RESULT_DIR/lib/pkgconfig:$PKG_CONFIG_PATH" ; export PKG_CONFIG_PATH
%endif

### Avoid el5 gcc bug
%{?el5:export CFLAGS="$CFLAGS -pthread"}
%{?el5:export CXXFLAGS="$CXXFLAGS -pthread"}
%ifarch i386
%{?el5:export CFLAGS="$CFLAGS -march=i486"}
%{?el5:export CXXFLAGS="$CXXFLAGS -march=i486"}
%endif

%configure --with-xmlrpc-c
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Manually install the man page to correct location for this release
%{__install} -p -m 0644 -D ./doc/rtorrent.1 %{buildroot}/%{_mandir}/man1/rtorrent.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/rtorrent.1*
%{_bindir}/rtorrent


%changelog
* Thu Aug 18 2011 Denis Fateyev <denis@fateyev.com> - 0.8.9-2
- Some fixes in spec for rtorrent-0.8.9

* Mon Aug 01 2011 Dag Wieers <dag@wieers.com> - 0.8.9-1
- Updated to release 0.8.9.

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
