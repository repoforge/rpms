# $Id$
# Authority: dries
# Upstream: <scandum$hotmail,com>

Summary: Console MUD client
Name: tintin
Version: 1.98.7
Release: 1
License: GPL
Group: Applications/Internet
URL: http://tintin.sourceforge.net/

Source: http://dl.sf.net/tintin/tintin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel

%description
TinTin++ is a MUD client that runs in console mode. A MUD is a
text based multi user dungeon.

%prep
%setup -n tt
%{__perl} -pi -e "s| /usr/bin| %{buildroot}%{_bindir}|g;" src/Makefile*

%build
%{__chmod} +x src/configure
cd src
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd src
%{__install} -d %{buildroot}%{_bindir}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING CREDITS FAQ INSTALL README TODO
%{_bindir}/tt++

%changelog
* Thu Dec 11 2008 Dries Verachtert <dries@ulyssis.org> - 1.98.7-1
- Updated to release 1.98.7.

* Mon Sep  1 2008 Dries Verachtert <dries@ulyssis.org> - 1.98.5-1
- Updated to release 1.98.5.

* Mon Aug 11 2008 Dries Verachtert <dries@ulyssis.org> - 1.98.4-1
- Updated to release 1.98.4.

* Wed Jul 16 2008 Dries Verachtert <dries@ulyssis.org> - 1.98.3-1
- Updated to release 1.98.3.

* Fri Jun 30 2008 Dries Verachtert <dries@ulyssis.org> - 1.98.2-1
- Updated to release 1.98.2.

* Sun Apr  6 2008 Dries Verachtert <dries@ulyssis.org> - 1.98.1-1
- Updated to release 1.98.1.

* Mon Mar 24 2008 Dries Verachtert <dries@ulyssis.org> - 1.98.0-1
- Updated to release 1.98.0.

* Sun Feb  3 2008 Dries Verachtert <dries@ulyssis.org> - 1.97.9-1
- Updated to release 1.97.9.

* Sun Nov 25 2007 Dries Verachtert <dries@ulyssis.org> - 1.97.8-1
- Updated to release 1.97.8.

* Sun Oct 21 2007 Dries Verachtert <dries@ulyssis.org> - 1.97.7-1
- Updated to release 1.97.7.

* Wed Oct 17 2007 Dries Verachtert <dries@ulyssis.org> - 1.97.6-1
- Updated to release 1.97.6.

* Fri Aug 17 2007 Dries Verachtert <dries@ulyssis.org> - 1.97.5-1
- Updated to release 1.97.5.

* Mon Jul 16 2007 Dries Verachtert <dries@ulyssis.org> - 1.97.4-1
- Updated to release 1.97.4.

* Sun Jul 08 2007 Dries Verachtert <dries@ulyssis.org> - 1.97.3-1
- Updated to release 1.97.3.

* Fri Jun 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.97.2-1
- Updated to release 1.97.2.

* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 1.97.0-1
- Updated to release 1.97.0.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 1.96.9-1
- Updated to release 1.96.9.

* Mon Mar 19 2007 Dries Verachtert <dries@ulyssis.org> - 1.96.7-1
- Updated to release 1.96.7.

* Tue Feb 13 2007 Dries Verachtert <dries@ulyssis.org> - 1.96.6-1
- Updated to release 1.96.6.

* Wed Dec 27 2006 Dries Verachtert <dries@ulyssis.org> - 1.96.5-1
- Updated to release 1.96.5.

* Fri Dec 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.96.4-1
- Updated to release 1.96.4.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.96.3-1
- Updated to release 1.96.3.

* Thu Aug 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.96.1-1
- Updated to release 1.96.1.

* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 1.95.9-1
- Updated to release 1.95.9.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.95.8-1
- Updated to release 1.95.8.

* Wed Jan  11 2006 Dries Verachtert <dries@ulyssis.org> - 1.95.7-1
- Updated to release 1.95.7.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.95.6-1
- Initial package.
