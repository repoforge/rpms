# $Id$
# Authority: dag

Summary: Alternative to the official libmatroska library
Name: libmkv
Version: 0.6.4
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://repo.or.cz/w/libmkv.git

Source: http://download.m0k.org/handbrake/contrib/libmkv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This library is meant to be an alternative to the official libmatroska library.
It is writen in plain C, and is intended to be very portable.

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
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%{_libdir}/libmkv.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libmkv.h
%{_libdir}/libmkv.so
%exclude %{_libdir}/libmkv.la

%changelog
* Mon Jul 27 2009 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Initial package. (using DAR)
