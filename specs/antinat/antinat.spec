# Authority: dag

### FIXME: Add sysv script using sysconfig file.

%define _datadir %{_libdir}

Summary: SOCKS4 and SOCKS5 compliant SOCKS server.
Name: antinat
Version: 0.66
Release: 0
License: GPL
Group: Applications/Internet
URL: http://yallara.cs.rmit.edu.au/~malsmith/products/antinat/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: antinat-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libds-devel >= 1.2.0
Requires: libds >= 1.2.0

%description
A SOCKS server for SOCKS v4 and SOCKS v5.

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
%{_libdir}/antinat-%{version}/

%changelog
* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 0.66-0
- Updated to release 0.66.

* Fri Sep 19 2003 Dag Wieers <dag@wieers.com> - 0.64-0
- Updated to release 0.64.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 0.63-0
- Initial package. (using DAR)
