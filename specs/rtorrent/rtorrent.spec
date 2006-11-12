# $Id$
# Authority: dries

Summary: Console based bittorrent client
Name: rtorrent
Version: 0.6.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://libtorrent.rakshasa.no

Source: http://libtorrent.rakshasa.no/downloads/rtorrent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libsigc++20-devel, ncurses-devel
BuildRequires: libtorrent-devel, curl-devel >= 7.12

%description
rTorrent is a console-based BitTorrent client. It aims to be a 
fully-featured and efficient client with the ability to run in the 
background using screen. It supports fast-resume and  session
management.

%prep
%setup

%build
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
