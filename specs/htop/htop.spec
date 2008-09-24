# $Id$
# Authority: dag
# Upstream: Hisham Muhammad <lode$gobolinux,org>
# Upstream: <htop-general$lists,sourceforge,net>

Summary: Interactive process viewer
Name: htop
Version: 0.8.1
Release: 1
License: GPL
Group: Applications/System
URL: http://htop.sourceforge.net/

Source: http://dl.sf.net/htop/htop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc >= 3.0, ncurses-devel

%description
htop is an interactive process viewer for Linux.

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
%doc %{_mandir}/man1/htop.1*
%{_bindir}/htop
%{_datadir}/applications/htop.desktop
%{_datadir}/pixmaps/htop.png

%changelog
* Tue Sep 23 2008 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Fri May 09 2008 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Sat Jun 02 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.6-1
- Updated to release 0.6.6.

* Thu Nov 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.5-1
- Updated to release 0.6.5.

* Sun Oct 08 2006 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Updated to release 0.6.4.

* Tue Jul 25 2006 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Updated to release 0.6.3.

* Sat May 20 2006 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Thu May 11 2006 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Thu Dec 29 2005 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.4-2
- Spec fixes.

* Sat Nov 12 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.4-1
- Updated to release 0.5.4.

* Tue Sep 20 2005 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Updated to release 0.5.3.

* Mon May 16 2005 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Sat Apr 09 2005 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Tue Aug 31 2004 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Tue Aug 24 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Sun Jun 20 2004 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Updated to release 0.3.2.

* Thu Jun 10 2004 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Updated to release 0.3.2.

* Sat May 29 2004 Dag Wieers <dag@wieers.com> - 0.3.1-1
- Updated to release 0.3.1.

* Wed May 19 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
