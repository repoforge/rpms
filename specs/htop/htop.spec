# $Id$
# Authority: dag
# Upstream: Hisham Muhammad <lode$gobolinux,org>
# Upstream: <htop-general$lists,sourceforge,net>

Summary: Interactive process viewer
Name: htop
Version: 0.5.3
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
#makeinstall
%{__install} -Dp -m0755 htop %{buildroot}%{_bindir}/htop
%{__install} -Dp -m0644 htop.1 %{buildroot}%{_mandir}/man1/htop.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/htop.1*
%{_bindir}/htop

%changelog
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
