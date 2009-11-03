# $Id$
# Authority: dag
# Upstream: Valery Reznic <valery_reznic$users,sf,net>

Summary: Convert dynamicly-linked ELF binaries into to "pseudo-static" binaries
Name: statifier
Version: 1.6.12
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://statifier.sourceforge.net/

Source: http://dl.sf.net/statifier/statifier-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 x86_64
Requires: binutils, gawk, gdb >= 5.2, sed

%description
Statifier create from dynamically linked ELF executable and all
it's libraries (and all LD_PRELOAD libraries if any) one file.
This file can be copied and run on another machine without need
to drag all it's libraries.

%prep
%setup

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|/usr/lib|\$(libdir)|g;
		s|/usr/bin|\$(bindir)|g;
		s|^(MAN_DIR_RPM).+$|$1=\$(mandir)|;
	' man/Makefile src/Makefile

%build
%{__make} %{?_smp_mflags} all \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL LICENSE NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/statifier/

%changelog
* Sun Sep 16 2007 Dries Verachtert <dries@ulyssis.org> - 1.6.12-1
- Updated to release 1.6.12.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 1.6.10-1
- Updated to release 1.6.10.

* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.8-1
- Updated to release 1.6.8.

* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 1.6.7-1
- Updated to release 1.6.7.

* Tue May 04 2004 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Tue Apr 20 2004 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Updated to release 1.1.0.

* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Initial package. (using DAR)
