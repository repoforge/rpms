# $Id$
# Authority: shuff
# Upstream: Thomas Bernard <miniupnp$free,fr>

Summary: NAT Port Mapping Protocol implementation
Name: libnatpmp
Version: 20131126
Release: 1%{?dist}
License: GPL
Group: Applications/
URL: http://miniupnp.free.fr/libnatpmp.html

Source: http://miniupnp.free.fr/files/libnatpmp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge

%description
libnatpmp is an attempt to make a portable and fully compliant implementation
of the protocol for the client side. It is based on non blocking sockets and
all calls of the API are asynchronous.

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
# multiarch support
%{__perl} -pi -e 's|/lib\b|/%{_lib}|g' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
PREFIX="%{buildroot}" %{__make} install 

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog.txt LICENSE README
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%exclude %{_libdir}/*.a

%changelog
* Sun Dec 22 2013 Steve Huff <shuff@vecna.org> - 20131126-1
- Initial package.
