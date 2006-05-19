# $Id$
# Authority: dries
# Upstream: Remi Denis-Courmont <remi-freshmeat$simphalempin,com>

Summary: Tunneling of Ipv6 over UDP through NATs
Name: miredo
Version: 0.8.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.simphalempin.com/dev/miredo/

Source: http://www.remlab.net/files/miredo/v0.8/miredo-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
iredo is an implementation of the "Teredo: Tunneling IPv6 over UDP
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
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man?/miredo*
%config(noreplace) %{_sysconfdir}/miredo-server.conf-dist
%config(noreplace) %{_sysconfdir}/miredo.conf
%config(noreplace) %{_sysconfdir}/miredo.conf-dist
%{_sbindir}/miredo
%{_sbindir}/miredo-checkconf
%{_sbindir}/miredo-server
%{_libdir}/libteredo.so.*
%{_libdir}/libtun6.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libteredo/
%{_includedir}/libtun6/
%{_libdir}/libteredo.so
%{_libdir}/libtun6.so
%exclude %{_libdir}/libteredo.la
%exclude %{_libdir}/libtun6.la

%changelog
* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.5-1
- Updated to release 0.8.5.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.4-1
- Initial package.
