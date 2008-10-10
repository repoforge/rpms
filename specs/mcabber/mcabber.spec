# $Id$
# Authority: dries
# Upstream: Mikael Berthe <mikael,berthe$lilotux,net>
# ScreenshotURL: http://www.lilotux.net/~mikael/mcabber/screenshots/mcabber_sample.png

Summary: Console jabber client
Name: mcabber
Version: 0.9.9
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.lilotux.net/~mikael/mcabber/

Source: http://www.lilotux.net/~mikael/mcabber/files/mcabber-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, ncurses-devel, glib2-devel, openssl-devel, pkgconfig

%description
Mcabber is a small jabber console client which supports SSL support, history
logging, external actions and more.

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
%doc %{_mandir}/man1/mcabber.1*
%{_bindir}/mcabber
%{_datadir}/mcabber/

%changelog
* Fri Oct 10 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.9-1
- Updated to release 0.9.9.

* Tue Oct  7 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.8-1
- Updated to release 0.9.8.

* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.7-1
- Updated to release 0.9.7.

* Sun Jan 13 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Tue Nov 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Mon Oct 29 2007 Dries Verachtert <dires@ulyssis.org> - 0.9.4-1
- Updated to release 0.9.4.

* Wed Jun 20 2007 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Wed Jun 13 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1
- Updated to release 0.9.2.

* Sun Feb 11 2007 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Mon Dec 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Updated to release 0.9.0.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.3-1
- Updated to release 0.8.3.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.2-1
- Updated to release 0.8.2.

* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Updated to release 0.8.1.

* Sun Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1
- Updated to release 0.8.0.

* Thu Jun 29 2006 Dag Wieers <dag@wieers.com> - 0.7.8-1
- Updated to release 0.7.8.

* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 0.7.6-1
- Updated to release 0.7.6.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.5-1
- Updated to release 0.7.5.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.4-1
- Updated to release 0.7.4.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 0.7.3-1
- Updated to release 0.7.3.

* Fri Dec 23 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Updated to release 0.7.2.

* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Updated to release 0.7.1.

* Mon Oct 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Updated to release 0.7.0.

* Tue Sep 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.8-1
- Updated to release 0.6.8.

* Fri Sep 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.7-1
- Updated to release 0.6.7.

* Thu Aug 18 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.6-1
- Updated to release 0.6.6.

* Wed Jul 27 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.5-1
- Updated to release 0.6.5.

* Thu Jul 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.4-1
- Updated to release 0.6.4.

* Wed Jul 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.3-1
- Updated to release 0.6.3.

* Tue Jul 12 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1
- Initial package.
