# $Id$
# Authority: dag
# Upstream: Christopher O'Brien <siege$preoccupied,net>

Summary: Lotus Sametime Community Client plugin for Gaim for Persona support
Name: gaim-meanwhile-ibm
Version: 1.0.1
Release: 2.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://w3.opensource.ibm.com/~meanwhile/

Source: http://w3.opensource.ibm.com/~meanwhile/yum/source/gaim-meanwhile-ibm-%{version}.tar.gz
NoSource: 0
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libghttp-devel, openldap-devel, gcc-c++, gaim-devel
Requires: gaim, libghttp, openldap, meanwhile >= 0.3, gaim-meanwhile
Obsoletes: meanwhile-gaim-persona <= %{version}, gaimblue <= %{version}

%description
Lotus Sametime Community Client plugin for Gaim for Persona support.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%dir %{_libdir}/gaim/
%exclude %{_libdir}/gaim/libpersona.a
%exclude %{_libdir}/gaim/libpersona.la
%{_libdir}/gaim/libpersona.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-2.2
- Rebuild for Fedora Core 5.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 1.0.1-2
- Rebuild against gaim 1.2.0-0.

* Thu Nov 16 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Sun Oct 17 2004 Dag Wieers <dag@wieers.com> - 1.0.0-2
- Build against gaim 1.0.1.

* Sun Oct 01 2004 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Fri Aug 17 2004 Dag Wieers <dag@wieers.com> - 0.81-2
- Build against gaim 0.82.

* Mon Aug 16 2004 Dag Wieers <dag@wieers.com> - 0.81-1
- Updated to release 0.81.

* Wed Jun 30 2004 Dag Wieers <dag@wieers.com> - 0.79-0.20040719
- Updated to CVS checkout 0.79cvs20040719.

* Wed Jun 30 2004 Dag Wieers <dag@wieers.com> - 0.79-0.20040630
- Initial package. (using DAR)
