# $Id$
# Authority: dag
# Upstream: <balance-general$lists,sourceforge,net>

Summary: TCP load-balancing proxy server
Name: balance
Version: 3.42
Release: 1
License: GPL
Group: Applications/Internet
URL: http://balance.sourceforge.net/

Source: http://www.inlab.de/balance-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: groff, ghostscript

%description
Balance is a simple but powerful generic tcp proxy with round robin
load balancing and failover mechanisms. Its behaviour can be controlled
at runtime using a simple command line syntax.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 balance %{buildroot}%{_sbindir}/balance
%{__install} -Dp -m0644 balance.1 %{buildroot}%{_mandir}/man1/balance.1

%{__install} -d -m1777 %{buildroot}%{_localstatedir}/run/balance/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man1/balance.1*
%{_sbindir}/balance

%defattr(-, root, root, 1777)
%{_localstatedir}/run/balance/

%changelog
* Sat Apr 12 2008 Dries Verachtert <dries@ulyssis.org> - 3.42-1
- Updated to release 3.42.

* Sat Dec  1 2007 Dries Verachtert <dries@ulyssis.org> - 3.40-1
- Updated to release 3.40.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 3.35-1
- Updated to release 3.35.

* Sun Mar 19 2006 Dag Wieers <dag@wieers.com> - 3.34-1
- Updated to release 3.34.

* Thu Nov 17 2005 Dries Verachtert <dries@ulyssis.org> - 3.32-1
- Updated to release 3.32.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> - 3.31-1
- Updated to release 3.31.

* Mon Aug 29 2005 Dries Verachtert <dries@ulyssis.org> - 3.26-1
- Updated to release 3.26.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 3.24-1
- Updated to release 3.24.

* Tue Jun 15 2004 Dag Wieers <dag@wieers.com> - 3.15-1
- Updated to release 3.15.

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 3.11-0
- Updated to release 3.11.

* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 3.6-0
- Initial package. (using DAR)
