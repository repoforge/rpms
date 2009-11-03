# $Id$
# Authority: dries
# Upstream: Michael Kohn <mike$mikekohn,net>

%define real_version 2006-11-14
%define lib_version 2006.11.14

Summary: Library for decompressing ZIP archives
Name: kunzip
Version: 0
Release: 0.20061114%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.mikekohn.net/kunzip.php

Source: http://downloads.mikekohn.net/programs/kunzip-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
kunzip is a small library for parsing and extracting zip files. Kunzip does 
not rely on any other libraries.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n kunzip

%build
%{__make} %{?_smp_mflags} default lib

%install
%{__rm} -rf %{buildroot}
%{__install} -D kunzip %{buildroot}%{_bindir}/kunzip
%{__install} -D libkunzip.so %{buildroot}%{_libdir}/libkunzip.so.%{lib_version}
%{__ln_s} libkunzip.so.%{lib_version} %{buildroot}%{_libdir}/libkunzip.so
%{__install} -D kunzip.h %{buildroot}%{_includedir}/kunzip.h

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc UNIX-README
%{_bindir}/kunzip
%{_libdir}/libkunzip.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/kunzip.h
%{_libdir}/libkunzip.so

%changelog
* Sat Dec 30 2006 Dries Verachtert <dries@ulyssis.org> - 0-0.20061114
- Initial package.
