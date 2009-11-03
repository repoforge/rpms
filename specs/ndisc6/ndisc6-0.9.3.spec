# $Id: ndisc6.spec 6146 2008-02-10 19:23:58Z dries $
# Authority: dries
# Upstream: Remi Denis-Courmont <rdenis$simphalempin,com>

Summary: Tools for ICMPv6 Neighbor&Router Discovery and TCP/IPv6 traceroute
Name: ndisc6
Version: 0.9.3
Release: 1%{?dist}
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

%build
%configure
%{__make} %{?_smp_mflags} 

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man8/ndisc6.8*
%doc %{_mandir}/man8/rdisc6.8*
%doc %{_mandir}/man8/tracert6.8*
%doc %{_mandir}/man8/tcptraceroute6.8*
%doc %{_mandir}/man8/rltraceroute6.8*
%doc %{_mandir}/man8/rdnssd.8*
%doc %{_mandir}/man1/tcpspray6.1*
%doc %{_mandir}/man1/addr2name.1*
%doc %{_mandir}/man1/name2addr.1*
%doc %{_mandir}/man1/dnssort.1*
%doc %{_mandir}/man1/tcpspray.1*
%{_bindir}/addr2name
%{_bindir}/name2addr
%{_bindir}/dnssort
%{_bindir}/tcpspray
%{_bindir}/ndisc6
%{_bindir}/rdisc6
%{_bindir}/tcpspray6
%{_bindir}/tracert6
%{_bindir}/rltraceroute6
%{_bindir}/tcptraceroute6
%dir %{_sysconfdir}/rdnssd/
%{_sysconfdir}/rdnssd/merge-hook
%{_sbindir}/rdnssd

%changelog
* Mon Aug 13 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.3-1
- Updated to release 0.9.3.

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
