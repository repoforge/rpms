# $Id$
# Authority: dries
# Upstream: Folkert Vanheusden <folkert@vanheusden.com>
# Screenshot: http://www.vanheusden.com/multitail/multitail.png

Summary: View one or multiple files like tail but with multiple windows
Name: multitail
Version: 3.2.3
Release: 1
License: GPL
Group: Applications/Text
URL: http://www.vanheusden.com/multitail/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.vanheusden.com/multitail/multitail-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, ncurses-devel
Requires: ncurses

%description
MultiTail lets you view one or multiple files like the original tail
program. The difference is that it creates multiple windows on your console
(with ncurses). Merging of 2 or even more logfiles is possible. It can also
use colors while displaying the logfiles (through regular expressions), for
faster recognition of what is important and what not. It can also filter
lines (again with regular expressions). It has interactive menus for editing
given regular expressions and deleting and adding windows.

%prep
%setup

%build
%{__make} %{?_smp_mflags}
#	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_sysconfdir}
%makeinstall \
	DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc readme.txt
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/multitail.conf
%{_bindir}/multitail

%changelog
* Sat Jul 17 2004 Dag Wieers <dag@wieers.com> - 3.2.3-1
- Updated to release 3.2.3.

* Sat May 22 2004 Dag Wieers <dag@wieers.com> - 3.2.1-1
- Updated to release 3.2.1.

* Wed May 19 2004 Dag Wieers <dag@wieers.com> - 3.2.0-1
- Updated to release 3.2.0.

* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 3.0.6-1
- Cosmetic changes.
- Updated to release 3.0.6.

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 3.0.3-1
- cleanup of spec file
- update to 3.0.3

* Sat Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 3.0.0-1
- first packaging for Fedora Core 1
