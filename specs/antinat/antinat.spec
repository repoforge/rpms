# $Id$
# Authority: dag
# Upstream: Malcolm Smith <malxau@users.sf.net>

### FIXME: Add sysv script using sysconfig file.

%define _datadir %{_libdir}

Summary: SOCKS4 and SOCKS5 compliant SOCKS server
Name: antinat
Version: 0.70
Release: 0
License: GPL
Group: Applications/Internet
URL: http://yallara.cs.rmit.edu.au/~malsmith/products/antinat/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

### FIXME: Source URL isn't clear about the filename, fails for wget and rpm. (Please fix upstream)
#Source: http://yallara.cs.rmit.edu.au/~malsmith/products/antinat/download.php?file=antinat-%{version}.tar.bz2
Source: antinat-%{version}.tar.bz2
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
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/antinat-%{version}/*/*.{a,la} \
		%{buildroot}%{_libdir}/antinat-%{version}/*/*/*.{a,la} \
		%{buildroot}%{_libdir}/antinat-%{version}/*/*/*/*.{a,la} \

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/antinat.conf
%{_bindir}/*
%{_libdir}/*.so*
%{_libdir}/antinat-%{version}/

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_includedir}/*.h
%exclude %{_libdir}/*.la

%changelog
* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 0.70-0
- Updated to release 0.70.

* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 0.66-0
- Updated to release 0.66.

* Fri Sep 19 2003 Dag Wieers <dag@wieers.com> - 0.64-0
- Updated to release 0.64.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 0.63-0
- Initial package. (using DAR)
