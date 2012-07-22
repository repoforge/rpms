# $Id$
# Authority: yury
# Upstream: Jari "Rakshasa" Sundell <sundell,software$gmail,com>

### Only build for RHEL5,6
# ExcludeDist: el2 el3 el4

# more unification with curl version (7.19.7 shipped with el6)
%define curl_version 7.19.7

%{?el5:%define _with_curl_static 1}


Name: rtorrent
# OpenSSL exception, see README
License: GPLv2+ with exceptions
Group: Applications/Internet
Version: 0.9.2
Release: 1%{?dist}
Summary: BitTorrent client based on libtorrent
URL: http://libtorrent.rakshasa.no/

Source0: http://libtorrent.rakshasa.no/downloads/%{name}-%{version}.tar.gz
Source3: http://curl.haxx.se/download/curl-%{curl_version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_with_curl_static:BuildRequires: curl-devel}

BuildRequires: libstdc++-devel
BuildRequires: libsigc++20-devel
BuildRequires: libtorrent-devel >= 0.13.2
BuildRequires: ncurses-devel
BuildRequires: pkgconfig
BuildRequires: libxml2-devel
BuildRequires: xmlrpc-c-devel >= 1.22
%{?el6:BuildRequires: cppunit}
%{?el6:BuildRequires: cppunit-devel}

Requires: libsigc++20
Requires: libtorrent >= 0.13.2
Requires: xmlrpc-c >= 1.22
Requires: xmlrpc-c-apps >= 1.22

%if %{?_with_curl_static:1}0
BuildRequires: openssl-devel
BuildRequires: libtool
BuildRequires: libidn-devel
%endif


%description
A BitTorrent client using libtorrent, which on high-bandwidth connections is 
able to seed at 3 times the speed of the official client. Using
ncurses its ideal for use with screen or dtach. It supports 
saving of sessions and allows the user to add and remove torrents and scanning
of directories for torrent files to seed and/or download.


%prep
%setup
%{?_with_curl_static:%setup -T -D -a 3}


%build
%if %{?_with_curl_static:1}0
# Build curl
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
    --with-gssapi="%{_prefix}/kerberos" \
    --with-libidn

%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" install
popd

# Append pkgconfig info
PKG_CONFIG_PATH="$RESULT_DIR/lib/pkgconfig:$PKG_CONFIG_PATH" ; export PKG_CONFIG_PATH
%endif

# avoid gcc-4.1 bug
%ifarch i386
    %{?el5:export CFLAGS="$CFLAGS -pthread -march=i486"}
    %{?el5:export CXXFLAGS="$CXXFLAGS -pthread -march=i486"}
%endif

%configure --with-xmlrpc-c
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# manually install the man page to correct location for this release
%{__install} -p -m 0644 -D ./doc/rtorrent.1 %{buildroot}/%{_mandir}/man1/rtorrent.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL README doc/faq.xml doc/rtorrent.rc
%{_bindir}/rtorrent
%{_mandir}/man1/rtorrent*

%changelog
* Mon May 07 2012 Denis Fateyev <denis@fateyev.com> - 0.9.2-1
- update to 0.9.2 version

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

* Thu Jan 1 2009 Dries Verachtert <dries@ulyssis.org> - 0.8.4-1
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
