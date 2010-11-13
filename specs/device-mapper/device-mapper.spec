# $Id$
# Authority: dag

### EL6 ships with device-mapper-devel-1.02.53-8.el6_0.2
### EL5 ships with device-mapper-1.02.39-1.el5_5.2
### EL4 ships with device-mapper-1.02.28-2.el4_8.1
# ExclusiveDist: el2 el3

%define _sbindir /sbin
%define _libdir /lib

Summary: Device mapper library
Name: device-mapper
Version: 1.00.07
Release: 0.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.sistina.com/

Source: ftp://ftp.sistina.com/pub/LVM2/device-mapper/%{name}.%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
This package contains the supporting userspace files (libdevmapper and
dmsetup) for the device-mapper.

%prep
%setup -n %{name}.%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Add version symlink
%{__ln_s} -f libdevmapper.so.1.00 %{buildroot}%{_libdir}/libdevmapper.so

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING COPYING.LIB README VERSION
%doc %{_mandir}/man?/*
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_sbindir}/*
%{_includedir}/*.h

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.00.07-0.2
- Rebuild for Fedora Core 5.

* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 1.00.07-0
- Initial package. (using DAR)
