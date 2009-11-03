# $Id$
# Authority: dries
# Upstream: Marc O. Gloor <mgloor$fhzv,ch>

# Screenshot: http://pubwww.fhzh.ch/~mgloor/data/screenie.jpg

Summary: Small frontend for screen
Name: screenie
Version: 1.30.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://pubwww.fhzh.ch/~mgloor/screenie.html

Source: http://pubwww.fhzh.ch/~mgloor/data/screenie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

%description
Screenie is a small and lightweight screen frontend that is
designed to be a session handler that simplifies the process
of administrating detached jobs by providing an interactive
menu.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 screenie %{buildroot}%{_bindir}/screenie

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/screenie

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.30.0-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 20 2005 Dries Verachtert <dries@ulyssis.org> - 1.30.0-1
- Updated to release 1.30.0.

* Wed Dec 07 2005 Dag Wieers <dag@wieers.com> - 1.26.0-2
- Fixed RPM Group.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.26.0-1
- Updated to release 1.26.0.

* Tue Sep 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.19.0-1
- Updated to release 1.19.0.

* Tue Aug 30 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
