# $Id$
# Authority: dries

%{?el4:%define _without_curl_pc 1}

Summary: Console based bittorrent client
Name: rtorrent
Version: 0.8.4
Release: 2
License: GPL
Group: Applications/Internet
URL: http://libtorrent.rakshasa.no/

Source: http://libtorrent.rakshasa.no/downloads/rtorrent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel >= 7.12
BuildRequires: gcc-c++
BuildRequires: libsigc++20-devel
BuildRequires: libtorrent-devel >= 0.12.0
BuildRequires: ncurses-devel

%description
rTorrent is a console-based BitTorrent client. It aims to be a 
fully-featured and efficient client with the ability to run in the 
background using screen. It supports fast-resume and session
management.

%prep
%setup

%build
### FIXME: Why does curl-compilation fail without the libsigc++20 includes on EL4 ?
%{?_without_curl_pc:export STUFF_CFLAGS="$(curl-config --cflags) $(pkg-config sigc++-2.0 --cflags)"}
%{?_without_curl_pc:export STUFF_LIBS="$(curl-config --libs) $(pkg-config sigc++-2.0 --libs) -ltorrent"}
%{?_without_curl_pc:export libcurl_CFLAGS="$(curl-config --cflags) $(pkg-config sigc++-2.0 --cflags)"}
%{?_without_curl_pc:export libcurl_LIBS="$(curl-config --libs) $(pkg-config sigc++-2.0 --libs) -ltorrent"}
%configure
%{__make} %{?_smp_mflags}

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
