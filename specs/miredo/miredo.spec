# $Id$
# Authority: dries
# Upstream: Rémi Denis-Courmont <rdenis$simphalempin,com>

Summary: Tunneling of Ipv6 over UDP through NATs
Name: miredo
Version: 1.1.7
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.simphalempin.com/dev/miredo/

Source: http://www.remlab.net/files/miredo/v0.8/miredo-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: judy-devel

%description
Miredo is an implementation of the "Teredo: Tunneling IPv6 over UDP
through NATs" proposed Internet standard (RFC4380). It can serve
either as a Teredo client, a stand-alone Teredo relay, or a Teredo
server. It is meant to provide IPv6 connectivity to hosts behind NAT
devices, most of which do not support IPv6, and not even
IPv6-over-IPv4 (including 6to4).

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__mkdir} rpmdocs
%{__mv} %{buildroot}%{_docdir}/miredo/examples/ rpmdocs/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO rpmdocs/*
%doc %{_mandir}/man?/miredo*
%doc %{_mandir}/man1/teredo-mire*
#doc %{_mandir}/man5/isatapd.conf*
#doc %{_mandir}/man8/isatapd*
%dir %{_sysconfdir}/miredo/
%config(noreplace) %{_sysconfdir}/miredo/miredo.conf
%config(noreplace) %{_sysconfdir}/miredo/client-hook
%{_sbindir}/miredo
%{_sbindir}/miredo-checkconf
%{_sbindir}/miredo-server
#{_sbindir}/isatapd
%{_bindir}/teredo-mire
%{_libdir}/libteredo.so.*
%{_libdir}/libtun6.so.*
%dir %{_libdir}/miredo/
%{_libdir}/miredo/miredo-privproc

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libteredo/
%{_includedir}/libtun6/
%{_libdir}/libteredo.so
%{_libdir}/libtun6.so
%{_libdir}/libteredo.a
%{_libdir}/libtun6.a
%exclude %{_libdir}/libteredo.la
%exclude %{_libdir}/libtun6.la

%changelog
* Tue Jul 21 2009 Dries Verachtert <dries@ulyssis.org> - 1.1.7-1
- Updated to release 1.1.7.

* Tue Apr 14 2009 Dries Verachtert <dries@ulyssis.org> - 1.1.6-1
- Updated to release 1.1.6.

* Sun Feb 17 2008 Dries Verachtert <dries@ulyssis.org> - 1.1.5-1
- Updated to release 1.1.5.

* Wed Nov 14 2007 Dries Verachtert <dries@ulyssis.org> - 1.1.4-1
- Updated to release 1.1.4.

* Tue Jan 09 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.6-1
- Updated to release 1.0.6.

* Mon Dec 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.5-1
- Updated to release 1.0.5.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1
- Updated to release 1.0.4.

* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Updated to release 1.0.0.

* Wed Aug 16 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.9-1
- Updated to release 0.9.9.

* Sun Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.8-1
- Updated to release 0.9.8.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.5-1
- Updated to release 0.8.5.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.4-1
- Initial package.
