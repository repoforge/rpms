# $Id$
# Authority: dag
# Upstream: Malcolm Smith <malxau@users.sf.net>

### FIXME: Add sysv script using sysconfig file.

%define _datadir %{_libdir}

Summary: SOCKS4 and SOCKS5 compliant SOCKS server
Name: antinat
Version: 0.71
Release: 1
License: GPL
Group: Applications/Internet
URL: http://yallara.cs.rmit.edu.au/~malsmith/products/antinat/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/antinat/antinat-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libds-devel >= 1.2.0
Requires: libds >= 1.2.0

%description
A SOCKS server for SOCKS v4 and SOCKS v5.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
export CFLAGS="%{optflags} -fPIC"
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README TODO
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*
%config(noreplace) %{_sysconfdir}/antinat.conf
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/antinat-%{version}/

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%exclude %{_libdir}/*.la
%exclude %{_libdir}/antinat-%{version}/*/*.la
%exclude %{_libdir}/antinat-%{version}/*/*/*.la
%exclude %{_libdir}/antinat-%{version}/*/*/*/*.la

%changelog
* Thu May 13 2004 Dag Wieers <dag@wieers.com> - 0.71-1
- Updated to release 0.71.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 0.70-0
- Updated to release 0.70.

* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 0.66-0
- Updated to release 0.66.

* Fri Sep 19 2003 Dag Wieers <dag@wieers.com> - 0.64-0
- Updated to release 0.64.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 0.63-0
- Initial package. (using DAR)
