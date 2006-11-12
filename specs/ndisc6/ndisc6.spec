# $Id$
# Authority: dries
# Upstream: Remi Denis-Courmont <rdenis$simphalempin,com>

Summary: Tools for ICMPv6 Neighbor&Router Discovery and TCP/IPv6 traceroute
Name: ndisc6
Version: 0.7.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.remlab.net/files/ndisc6/

Source: http://www.remlab.net/files/ndisc6/ndisc6-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package consists of two programs:
- ndisc6, which performs ICMPv6 Neighbor Discovery in userland,
- rdisc6, which performs ICMPv6 Router Discovery in userland.

%prep
%setup
#%{__perl} -pi -e 's|\)/man/man8/|)/share/man/man8/|g;' Makefile
# make sure 'install' doesn't depend on 'all'
#%{__perl} -pi -e 's|install: all|install: |g;' Makefile

%build
%configure
%{__make} %{?_smp_mflags} 
#ndisc6 rdisc6 traceroute6

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_mandir}/man8 %{buildroot}%{_bindir}
%makeinstall #DESTDIR=%{buildroot}
%{__rm} -f %{buildroot}%{_mandir}/man8/tcptraceroute6.8
%{__ln_s} %{_mandir}/man8/traceroute6.8 %{buildroot}%{_mandir}/man8/tcptraceroute6.8
%{__rm} -f %{buildroot}%{_mandir}/man8/tracert6.8
%{__ln_s} %{_mandir}/man8/rltraceroute6.8 %{buildroot}%{_mandir}/man8/tracert6.8
%{__rm} -f %{buildroot}%{_mandir}/man1/nameinfo.1
%{__ln_s} %{_mandir}/man1/addrinfo.1 %{buildroot}%{_mandir}/man1/nameinfo.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man8/ndisc6.8*
%doc %{_mandir}/man8/rdisc6.8*
%doc %{_mandir}/man8/tracert6.8*
%doc %{_mandir}/man8/tcptraceroute6.8*
%doc %{_mandir}/man8/rltraceroute6.8*
%doc %{_mandir}/man1/tcpspray6.1*
%doc %{_mandir}/man1/addrinfo*
%doc %{_mandir}/man1/dnssort*
%doc %{_mandir}/man1/nameinfo*
%{_bindir}/addrinfo
%{_bindir}/dnssort
%{_bindir}/nameinfo
%{_bindir}/ndisc6
%{_bindir}/rdisc6
%{_bindir}/tcpspray6
%{_bindir}/tracert6
%{_bindir}/rltraceroute6
%{_bindir}/tcptraceroute6

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Updated to release 0.7.1.

* Sun Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.7-1
- Updated to release 0.6.7.

* Tue Aug 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.6-1
- Updated to release 0.6.6.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1
- Updated to release 0.6.2.

* Thu Apr 27 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.0-1
- Updated to release 0.6.0.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.1-2
- Fix in the summary and the url, thanks to Hugo van der Kooij.

* Thu Dec 01 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.1-1
- Updated to release 0.5.1.

* Wed Nov 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Initial package.
