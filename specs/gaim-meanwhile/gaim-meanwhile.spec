# $Id$
# Authority: dag
# Upstream: Christopher O'Brien <siege$preoccupied,net>

Summary: Lotus Sametime Community Client plugin for Gaim
Name: gaim-meanwhile
Version: 1.2.8
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://meanwhile.sourceforge.net/

Source: http://dl.sf.net/meanwhile/gaim-meanwhile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gaim-devel >= 1.2.1, meanwhile-devel >= 0.4.1, gcc-c++
BuildRequires: pkgconfig, glib2-devel
Obsoletes: meanwhile-gaim <= %{version}

%description
Lotus Sametime Community Client plugin for Gaim

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%dir %{_libdir}/gaim/
%{_libdir}/gaim/libmwgaim.so
%exclude %{_libdir}/gaim/libmwgaim.la
%{_datadir}/pixmaps/gaim/

%changelog
* Sun Mar 05 2007 Dag Wieers <dag@wieers.com> - 1.2.8-1
- Updated to release 1.2.8.

* Sun Nov 27 2005 Dag Wieers <dag@wieers.com> - 1.2.5-1
- Updated to release 1.2.5.

* Sat May 21 2005 Dag Wieers <dag@wieers.com> - 1.2.2-2
- Rebuild against gaim 1.3.0-1 (FC3).

* Fri May 06 2005 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Fri Mar 11 2005 Dag Wieers <dag@wieers.com> - 1.0.2-2
- Rebuild against gaim 1.1.4-1.

* Thu Nov 18 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Sun Oct 31 2004 Dag Wieers <dag@wieers.com> - 1.0.1-2
- Build against gaim 1.0.2.

* Sun Oct 17 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Thu Sep 23 2004 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0 .

* Fri Aug 27 2004 Dag Wieers <dag@wieers.com> - 0.82-1
- Updated to release 0.82.

* Mon Aug 16 2004 Dag Wieers <dag@wieers.com> - 0.81-1
- Updated to release 0.81.

* Mon Jul 19 2004 Dag Wieers <dag@wieers.com> - 0.80-1
- Updated to release 0.80.

* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 0.79-1
- Updated to release 0.79.

* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 0.78-1
- Initial package. (using DAR)
