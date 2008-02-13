# $Id$
# Authority: dries
# Upstream: <tujikawa$rednoah,com>

Summary: Download utility with BitTorrent and Metalink support
Name: aria2
Version: 0.12.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://aria2.sourceforge.net/

Source: http://dl.sf.net/aria2/aria2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, openssl-devel, libxml2-devel, pkgconfig

%description
aria2 is a download utility with resuming and segmented downloading.
Supported protocols are HTTP/HTTPS/FTP/BitTorrent/Metalink.

%prep
%setup
 
%build
### Add correct CFLAGS for EL3 and RH9
%{expand: %%define optflags %{optflags} %(pkg-config --cflags openssl)}
#export CPPFLAGS="-I/usr/include/libxml2 $(pkg-config --cflags openssl)"
%configure \
    --disable-xmltest \
    --enable-metalink
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang aria2c
%{__rm} -f %{buildroot}%{_datadir}/locale/locale.alias

%clean
%{__rm} -rf %{buildroot}
  
%files -f aria2c.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS README AUTHORS TODO
%doc %{_mandir}/man1/aria2c.1*
%{_bindir}/aria2c

%changelog
* Mon Feb 11 2008 Dag Wieers <dag@wieers.com> - 0.12.1-1
- Updated to release 0.12.1.

* Mon Dec 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.12.0-1
- Updated to release 0.12.0.

* Tue Nov 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.5-1
- Updated to release 0.11.5.

* Mon Oct 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.4-1
- Updated to release 0.11.4.

* Sun Sep 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.3-1
- Updated to release 0.11.3.

* Fri Aug 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.2-1
- Updated to release 0.11.2.

* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.1-1
- Updated to release 0.11.1.

* Tue Jun 12 2007 Dag Wieers <dag@wieers.com> - 0.11.0-1
- Updated to release 0.11.0.

* Tue May 15 2007 Dag Wieers <dag@wieers.com> - 0.10.2.1-1
- Updated to release 0.10.2.1.

* Wed Mar 28 2007 Dries Verachtert <dries@ulyssis.org> - 0.10.2-1
- Updated to release 0.10.2.

* Tue Feb 13 2007 Dries Verachtert <dries@ulyssis.org> - 0.10.1-1
- Updated to release 0.10.1.

* Mon Jan 29 2007 Dag Wieers <dag@wieers.com> - 0.10.0-1
- Updated to release 0.10.0.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Updated to release 0.9.0.

* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 0.8.1-2
- Fixed group name.

* Mon Oct 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Updated to release 0.8.1.

* Mon Aug 21 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Updated to release 0.7.2.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org>
- Updated to release 0.7.1.

* Sat Aug 12 2006 Dries Verachtert <dries@ulyssis.org>
- Updated to release 0.7.0.

* Fri Jul 28 2006 Anthony Bryan <anthonybryan@gmail.com>
- Update to version 0.6.0+1 and FC6
 
* Mon Jun 5 2006 Malcolm A Hussain-Gambles <malcolm@secpay7.force9.co.uk>
- First release of this package by me
