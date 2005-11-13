# $Id$
# Authority: dries
# Upstream: Remi Denis-Courmont <rdenis$simphalempin,com>

Summary: Tools for ICMPv7 Neighbor&Router Discovery and TCP/IPv6 traceroute
Name: ndisc6
Version: 0.4.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://people.via.ecp.fr/~rem/ndisc6/

Source: http://people.via.ecp.fr/~rem/ndisc6/ndisc6-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package consists of two programs:
- ndisc6, which performs ICMPv6 Neighbor Discovery in userland,
- rdisc6, which performs ICMPv6 Router Discovery in userland.

%prep
%setup
%{__perl} -pi -e 's|\)/man/man8/|)/share/man/man8/|g;' Makefile
# make sure 'install' doesn't depend on 'all'
%{__perl} -pi -e 's|install: all|install: |g;' Makefile

%build
%{__make} %{?_smp_mflags} ndisc6 rdisc6

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_mandir}/man8
%makeinstall #DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man?/*disc6*
%{_bindir}/ndisc6
%{_bindir}/rdisc6

%changelog
* Wed Nov 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Initial package.
