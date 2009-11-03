# $Id$
# Authority: dries
# Upstream: Folkert Vanheusden <folkert$vanheusden,com>
# Screenshot: http://www.vanheusden.com/multitail/multitail.png

%define desktop_vendor rpmforge

Summary: View one or multiple files like tail but with multiple windows
Name: multitail
Version: 5.2.2
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.vanheusden.com/multitail/

Source: http://www.vanheusden.com/multitail/multitail-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: make, ncurses-devel
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
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}
%{__make} install DESTDIR="%{buildroot}"

### Prepare documentation
%{__install} -d -m0755 scripts/
%{__install} -p -m0644 *.pl *.sh scripts/

### We don't want rpm to require on geoip, so remove it
%{__rm} -f %{buildroot}%{_sysconfdir}/multitail/convert-geoip.pl

### Clean up buildroot
%{__mv} -f %{buildroot}%{_sysconfdir}/multitail.conf.new %{buildroot}%{_sysconfdir}/multitail.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL *.conf *.html *.txt scripts/
%doc %{_mandir}/man1/multitail.1*
%config(noreplace) %{_sysconfdir}/multitail.conf
%{_bindir}/multitail
%dir %{_sysconfdir}/multitail/
%{_sysconfdir}/multitail/colors-example.pl
%{_sysconfdir}/multitail/colors-example.sh
%{_sysconfdir}/multitail/convert-simple.pl

%changelog
* Tue May 20 2008 Dries Verachtert <dries@ulyssis.org> - 5.2.2-1
- Updated to release 5.2.2.

* Sat Feb 23 2008 Dries Verachtert <dries@ulyssis.org> - 5.2.1-1
- Updated to release 5.2.1.

* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 5.2.0-1
- Updated to release 5.2.0.

* Sat Jun 09 2007 Dag Wieers <dag@wieers.com> - 5.0.5-1
- Updated to release 5.0.5.

* Sat Jun 02 2007 Dag Wieers <dag@wieers.com> - 5.0.4-1
- Updated to release 5.0.4.

* Thu May 10 2007 Dag Wieers <dag@wieers.com> - 5.0.3-1
- Updated to release 5.0.3.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 5.0.2-1
- Updated to release 5.0.2.

* Fri Apr 27 2007 Dag Wieers <dag@wieers.com> - 5.0.1-1
- Updated to release 5.0.1.
- Removed perl-Geo-IP from dependencies by moving it to %%doc. (Michael Mansour)

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 5.0.0-1
- Updated to release 5.0.0.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 4.2.0-1
- Updated to release 4.2.0.

* Fri Jun 09 2006 Dag Wieers <dag@wieers.com> - 4.0.5-1
- Updated to release 4.0.5.

* Tue May 23 2006 Dag Wieers <dag@wieers.com> - 4.0.4-1
- Updated to release 4.0.4.

* Tue Mar 28 2006 Dag Wieers <dag@wieers.com> - 3.8.10-1
- Updated to release 3.8.10.

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 3.8.9-1
- Updated to release 3.8.9.

* Sat Feb 18 2006 Dag Wieers <dag@wieers.com> - 3.8.6-1
- Updated to release 3.8.6.

* Mon Jan 30 2006 Dries Verachtert <dries@ulyssis.org> - 3.8.5-1
- Updated to release 3.8.5.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 3.8.4-1
- Updated to release 3.8.4.

* Wed Jan 04 2006 Dag Wieers <dag@wieers.com> - 3.8.3-1
- Updated to release 3.8.3.

* Sun Jan 01 2006 Dries Verachtert <dries@ulyssis.org> - 3.8.2-1
- Updated to release 3.8.2.

* Tue Dec 27 2005 Dries Verachtert <dries@ulyssis.org> - 3.8.0-1
- Updated to release 3.8.0.

* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> - 3.7.6-1
- Updated to release 3.7.6.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 3.7.5-1
- Updated to release 3.7.5.

* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> - 3.7.4-1
- Updated to release 3.7.4.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> - 3.7.3-1
- Updated to release 3.7.3.

* Mon Oct 03 2005 Dries Verachtert <dries@ulyssis.org> - 3.7.2-1
- Updated to release 3.7.2.

* Mon Aug 1 2005 Dries Verachtert <dries@ulyssis.org> - 3.6.0-1
- Updated to release 3.6.0.

* Fri Jul 22 2005 Dries Verachtert <dries@ulyssis.org> - 3.6.0-0.rc2
- Updated to release 3.6.0rc2.

* Mon Jul 18 2005 Dries Verachtert <dries@ulyssis.org> - 3.6.0-0.rc1
- Updated to release 3.6.0rc1.

* Mon Jul 18 2005 Dries Verachtert <dries@ulyssis.org> - 3.5.7-1
- Updated to release 3.5.7.

* Sun Mar 01 2005 Dries Verachtert <dries@ulyssis.org> - 3.4.8-1
- Updated to release 3.4.8.

* Sun Jan 23 2005 Dries Verachtert <dries@ulyssis.org> - 3.4.5-1
- Updated to release 3.4.5.

* Sun Jan 16 2005 Dries Verachtert <dries@ulyssis.org> - 3.4.4-1
- Updated to release 3.4.4.

* Sun Dec 26 2004 Dries Verachtert <dries@ulyssis.org> - 3.4.3-1
- Updated to release 3.4.3.

* Sun Nov 28 2004 Dries Verachtert <dries@ulyssis.org> - 3.4.2-1
- Updated to release 3.4.2.

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 3.4.1-1
- Updated to release 3.4.1.

* Mon Oct 18 2004 Dries Verachtert <dries@ulyssis.org> - 3.4.0-1
- Updated to release 3.4.0.

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
