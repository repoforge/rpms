# $Id$

# Authority: dag

# Upstream: Dug Song <dugsong@monkey.org>

Summary: A simple portable interface to lowlevel networking routines.
Name: libdnet
Version: 1.7
Release: 0
License: BSD-like
Group: System Environment/Libraries
URL: http://libdnet.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/libdnet/libdnet-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Libdnet provides a simple portable interface to lowlevel networking routines.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} \
	COPTFLAG="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*.a
%{_includedir}/*.h
%{_includedir}/dnet/

%changelog
* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 1.7-0
- Initial package. (using DAR)
